#coding=utf-8

from b2 import object2


def test():
    """Http 状态返回码
        Test:
            >>> HTTP_CODE.ok == 200
            >>> HTTP_CODE.created == 201
            >>> HTTP_CODE.unsupported_media_type == 415
            >>> print HTTP_CODE.unsupported_media_type
            >>> HTTP_CODE.not_extended == 510
            >>> print HTTP_CODE.not_extended
            >>> FILTER_PRIORITY.NONE == 0
               True
    """
    pass


FILTER_PRIORITY = object2.enum2(
    HIGHEST=100,
    VERY_HIGH=90,
    HIGH=80,
    MIDDLE=70,
    LOW=60,
    VERY_LOW=50,
    LOWEST=40,
    NONE=0)

HTTP_CODE = object2.enum(
    "continue=100 swiching_protocols \
        ok=200 created accepted non_auth no_content reset_content partial_content \
        multiple_choice=300 moved_permanently found use_proxy unused temporary_redirect \
        bad_request=400 unauthorized payment_required forbidden not_found method_not_allowed not_accpetable proxy_auth_required request_timeout conflict gone length_required \
        precondition_faild request_entity_too_large request_url_too_long unsupported_media_type request_range_not_satisafiable expectation_failed i_m_a_teapot \
        too_many_connections unprocessable_entity failed_dependency unordered_collection upgrade_required retry_with \
        internal_server_error=500 not_implemented bad_gateway service_unavailable getway_timeout http_version_not_supported variant_also_negotiates insufficient_storage \
        bandwidth_limit_exceeded=509 not_extended",
    split_char="=")
