#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Response(SimpleTemplateResponse):
    """
    An HttpResponse that allows its data to be rendered into
    arbitrary media types.
    """

    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        """
        Alters the init arguments slightly.
        For example, drop 'template_name', and instead use 'data'.

        Setting 'renderer' and 'media_type' will typically be deferred,
        For example being set automatically by the `APIView`.
        名称进行了部分调整，然后更多的是依靠父类的实现方法。
        """
        super(Response, self).__init__(None, status=status)

        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)

        self.data = data
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value

    @property
    def rendered_content(self):
        """
        用于渲染的文本内容，
        对于不同的媒体类型进行的不同的操作处理，然后渲染器将属性进行渲染返回
        """
        renderer = getattr(self, 'accepted_renderer', None)
        accepted_media_type = getattr(self, 'accepted_media_type', None)
        context = getattr(self, 'renderer_context', None)

        assert renderer, ".accepted_renderer not set on Response"
        assert accepted_media_type, ".accepted_media_type not set on Response"
        assert context is not None, ".renderer_context not set on Response"
        context['response'] = self

        media_type = renderer.media_type
        charset = renderer.charset
        content_type = self.content_type

        if content_type is None and charset is not None:
            content_type = "{0}; charset={1}".format(media_type, charset)
        elif content_type is None:
            content_type = media_type
        self['Content-Type'] = content_type

        ret = renderer.render(self.data, accepted_media_type, context)
        if isinstance(ret, six.text_type):
            assert charset, (
                'renderer returned unicode, and did not specify '
                'a charset value.'
            )
            return bytes(ret.encode(charset))

        if not ret:
            del self['Content-Type']

        return ret

    @property
    def status_text(self):
        """
        Returns reason text corresponding to our HTTP response status code.
        Provided for convenience.
        返回指定的状态码信息
        """
        return responses.get(self.status_code, '')

    def __getstate__(self):
        """
        Remove attributes from the response that shouldn't be cached.
        移除返回信息中部分不需要进行缓存的属性
        """
        state = super(Response, self).__getstate__()
        for key in (
            'accepted_renderer', 'renderer_context', 'resolver_match',
            'client', 'request', 'json', 'wsgi_request'
        ):
            if key in state:
                del state[key]
        state['_closable_objects'] = []
        return state
