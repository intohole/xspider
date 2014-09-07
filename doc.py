# coding=utf-8
#!/usr/bin/env python


import time


class Doc(object):
    '''
    用于生成ｍｄ文档
    '''

    def __init__(self, title, content, author,  category, tags=[], summary=None, head_date=None):
        if head_date == None:
            self.head_date = time.strftime('%Y-%m-%d %H:%M:%S')
        if title and len(title) >= 3:
            self.title = title
        else:
            raise ValueError, 'title is string and not empty'
        if content and len(content) >= 50:
            self.content = content
        else:
            raise ValueError, 'content is string and len must be bigger than 50'
        if content and len(author) > 0:
            self.author = author
        else:
            raise ValueError, 'author type is string and len must be bigger than 0'
        print tags
        if tags is not None and isinstance(tags, (list, tuple)):
            self.tags = ' ,'.join(tags)
        else:
            print tags , type(tags)
            raise TypeError, 'tags type is list or tuple'
        if category and len(category) > 0:
            self.category = category
        else:
            raise ValueError, 'category type is string and len must be bigger than 0'
        self.file_name = title
        self.summary = summary

    def __str__(self):
        msg = []
        msg.append('Date:%s  \n' % self.head_date)
        msg.append('Title:%s  \n' % self.title)
        msg.append('Author:%s  \n' % self.author)
        msg.append('Category:%s  \n' % self.category)
        msg.append('Tags:%s  \n' % self.tags)
        if self.summary:
            msg.append('Summary:%s  \n' % self.summary)
            msg.append(
                '<div class="msummary">&nbsp&nbsp<h3>摘要<h3>: %s</div>  \n' %
                self.summary)
        msg.append('  %s' % self.content)
        return ''.join(msg)


if __name__ == '__main__':
    doc = Doc('test', 'cool', 'li', 'jiji',  ['1', '2'], '摘要')
    print doc
