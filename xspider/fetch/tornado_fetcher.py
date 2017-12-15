import logging
import copy
import json
import time

from xspider.model.models import ZResponse
import tornado.httpclient
from tornado.curl_httpclient import CurlAsyncHTTPClient
import tornado.ioloop


def text(obj, encoding='utf-8'):
    if isinstance(obj, unicode):
        return obj.encode(encoding)
    return obj


def unicode_obj(obj, encoding='utf-8'):
    if isinstance(obj, str):
        return obj.decode(encoding)
    return obj


class Fetcher(object):
    default_options = {
        'method': 'GET',
        'headers': {},
        'allow_redirects': True,
        'use_gzip': True,
        'timeout': 120,
    }

    def __init__(self,
                 phantomjs_proxy='http://localhost:25555',
                 pool_size=100,
                 async=False):
        self.phantomjs_proxy = phantomjs_proxy
        self.async = async
        if self.async:
            self.http_client = CurlAsyncHTTPClient(
                max_clients=pool_size, io_loop=tornado.ioloop.IOLoop())
        else:
            self.http_client = tornado.httpclient.HTTPClient(
                max_clients=pool_size)

    @staticmethod
    def parse_option(default_options, url, user_agent, **kwargs):
        fetch = copy.deepcopy(default_options)
        fetch['url'] = url
        fetch['headers']['User-Agent'] = user_agent
        js_script = kwargs.get('js_script')
        if js_script:
            fetch['js_script'] = js_script
            fetch['js_run_at'] = kwargs.get('js_run_at', 'document-end')
        fetch['load_images'] = kwargs.get('load_images', False)
        return fetch

    def request(self, req, method='get', *argv, **kw):
        start_time = time.time()
        fetch = self.parse_option(
            self.default_options,
            req.url,
            user_agent=req.headers["User-Agent"],
            **kw)
        request_conf = {'follow_redirects': False}
        if 'timeout' in fetch:
            request_conf['connect_timeout'] = fetch['timeout']
            request_conf['request_timeout'] = fetch['timeout'] + 1

        def handle_response(response):
            if not response.body:
                return handle_error(Exception('no response from phantomjs'))
            try:
                result = json.loads(text(response.body))
                if response.error:
                    result['error'] = text(response.error)
            except Exception as e:
                return handle_error(e)

            if result.get('status_code', 200):
                logging.info('[%d] %s %.2fs', result['status_code'], req.url,
                             result['cost_time'])
            else:
                logging.error('[%d] %s, %r %.2fs', result['status_code'],
                              req.url, result['content'], result['cost_time'])
            return ZResponse(
                req.url,
                req.pre_url,
                redirect_url=result["url"],
                status_code=result["status_code"],
                raw_text=result["content"],
                cost_time=result["cost_time"],
                error=result["error"])

        def handle_error(error):
            result = ZResponse(
                req.url,
                req.pre_url,
                status_code=getattr(error, 'code', 599),
                error=unicode_obj(error),
                raw_text=None,
                cost_time=time.time() - start_time,
                crawl_time=start_time)
            logging.error('[%d] %s, %r %.2fs', result.status_code, req.url,
                          error, result.crawl_time)
            return result

        try:
            request = tornado.httpclient.HTTPRequest(
                url='%s' % self.phantomjs_proxy,
                method='POST',
                body=json.dumps(fetch),
                **request_conf)
            if self.async:
                self.http_client.fetch(request, handle_response)
            else:
                return handle_response(self.http_client.fetch(request))
        except tornado.httpclient.HTTPError as e:
            if e.response:
                return handle_response(e.response)
            else:
                return handle_error(e)
        except Exception as e:
            return handle_error(e)


if __name__ == '__main__':
    fetcher = Fetcher()
    from xspider.model.models import ZRequest
    request = ZRequest("http://buyiker.com", "x", 3)
    print fetcher.request(request)
