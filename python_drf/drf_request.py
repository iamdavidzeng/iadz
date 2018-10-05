#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Empty(object):
    """
    在无法使用None的位置，作为一个不设置属性的类占位符使用。
    """


class ForcedAuthentication(object):
    """
    This authentication class is used if the test client or request factory
    forcibly authenticated the request.
    一个用于客户端或者请求工厂被强制要求认证请求的认证器。
    """

    def __init__(self, force_user, force_token):
        self.force_user = force_user
        self.force_token = force_token

    def authenticate(self, request):
        return (self.force_user, self.force_token)


def is_form_media_type(media_type):
    """
    Return True if the media type is a valid form media type.
    如果解析后的媒体类型符合媒体类型格式要求则返回True
    """
    base_media_type, params = parse_header(media_type.encode(HTTP_HEADER_ENCODING))
    return (base_media_type == 'application/x-www-form-urlencoded' or
            base_media_type == 'multipart/form-data')


class Request(object):
    """
    标准的HttpRequest实例将被这个类强化，
    在初始化过程当中，有部分关键字参数被指明了类型：
        request(HttpRequest): 原生的request实例
        parsers_classes(list/tuple): 用于解析请求内容的解析类列表
        authentication_classes(list/tuple): 用于对请求用户进行认证的认证类列表
    """

    def __init__(self, request, parsers=None, authenticators=None, 
                 negotiator=None, parser_context=None)
        """
        对象属性进行初始化，negotiator若为None则使用设置中默认的类，解析内容中将会更新
        两个键值对，用于将self本身和请求的编码格式或者设置中的默认编码格式放入其中，
        如果请求属性中存在用于强制要求认证的用户或者认证信息属性，就会生成一个认证器实例，
        覆盖原来的认证器。
        """
        self._request = request
        self.parsers = parsers or ()
        self.authenticators = authenticators or ()
        self.negotiator = negotiator or self._default_negotiator()
        self.parser_context = parser_context
        self._data = Empty
        self._files = Empty
        self._full_data = Empty
        self._content_type = Empty
        self._stream = Empty

        if self.parser_context is None:
            self.parser_context = {}
        self.parser_context['request'] = self
        self.parser_context['encoding'] = request.encoding or settings.DEFAULT_CHARSET

        force_user = getattr(request, '_force_auth_user', None)
        force_token = getattr(request, '_force_auth_token', None)
        if force_user is not None or force_token is not None:
            forced_auth = ForcedAuthentication(force_user, force_token)
            self.authenticators = (forced_auth,)

    def _default_negotiator(self):
        """
        读取设置中默认的内容协调类
        """
        return api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS()

    @property
    def content_type(self):
        """
        从请求头部中获取内容类型
        """
        meta = self._request.META
        return meta.get('CONTENT_TYPE', meta.get('HTTP_CONTENT_TYPE', ''))

    @property
    def stream(self):
        """
        Returns an object that may be used to stream the request content.
        返回一个将请求内容解析成数据流的对象
        """
        if not _hasattr(self, '_stream'):
            self._load_stream()
        return self._stream

    @property
    def query_params(self):
        """
        More semantically correct name for request.GET.
        使用一个更符合语义的数据名称带代替request.GET
        """
        return self._request.GET

    @property
    def data(self):
        """
        调用方法实现将请求中的文本内容和文件信息存放在类的data属性中
        """
        if not _hasattr(self, '_full_data'):
            self._load_data_and_files()
        return self._full_data

    @property
    def user(self):
        """
        Returns the user associated with the current request, as authenticated
        by the authentication classes provided to the request.
        如果类属性中没有_user属性，则调用类中的认证方法对于_user属性进行初始化
        """
        if not hasattr(self, '_user'):
            self._authenticate()
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the user on the current request. This is necessary to maintain
        compatibility with django.contrib.auth where the user property is
        set in the login and logout functions.

        Note that we also set the user on Django's underlying `HttpRequest`
        instance, ensuring that it is available to any middleware in the stack.
        提供一个设置用户属性的方法
        """
        self._user = value
        self._request.user = value

    @property
    def auth(self):
        """
        Returns any non-user authentication information associated with the
        request, such as an authentication token.
        调用认证方法对于认证信息进行初始化
        """
        if not hasattr(self, '_auth'):
            self._authenticate()
        return self._auth

    @auth.setter
    def auth(self, value):
        """
        Sets any non-user authentication information associated with the
        request, such as an authentication token.
        提供一个设置认证信息的方法
        """
        self._auth = value
        self._request.auth = value

    @property
    def successful_authenticator(self):
        """
        Return the instance of the authentication instance class that was used
        to authenticate the request, or `None`.
        若无_authenticator属性则调用类属性中的认证器对请求进行认证并对_authenticator属性
        进行初始化。
        """
        if not hasattr(self, '_authenticator'):
            self._authenticate()
        return self._authenticator

    def _load_data_and_files(self):
        """
        Parses the request content into `self.data`.
        解析请求中的文本内容和文件至self.data属性中
        """
        if not _hasattr(self, '_data'):
            self._data, self._files = self._parse()
            if self._files:
                self._full_data = self._data.copy()
                self._full_data.update(self._files)
            else:
                self._full_data = self._data

            # copy files refs to the underlying request so that closable
            # objects are handled appropriately.
            self._request._files = self._files

    def _load_stream(self):
        """
        Return the content body of the request, as a stream.
        确认用作数据流的内容实体
        """
        meta = self._request.META
        try:
            content_length = int(
                meta.get('CONTENT_LENGTH', meta.get('HTTP_CONTENT_LENGTH', 0))
            )
        except (ValueError, TypeError):
            content_length = 0

        if content_length == 0:
            self._stream = None
        elif not self._request._read_started:
            self._stream = self._request
        else:
            self._stream = six.BytesIO(self.body)

    def _supports_form_parsing(self):
        """
        Return True if this requests supports parsing form data.
        迭代类解析器，若类的解析器属性中有符合制定媒体类型要求的，返回True
        """
        form_media = (
            'application/x-www-form-urlencoded',
            'multipart/form-data'
        )
        return any([parser.media_type in form_media for parser in self.parsers])

    def _parse(self):
        """
        Parse the request content, returning a two-tuple of (data, files)

        May raise an `UnsupportedMediaType`, or `ParseError` exception.
        解析请求内容，将文本内容和文件内容作为一个元组进行返回。
        """
        media_type = self.content_type
        try:
            stream = self.stream
        except RawPostDataException:
            if not hasattr(self._request, '_post'):
                raise
            # If request.POST has been accessed in middleware, and a method='POST'
            # request was made with 'multipart/form-data', then the request stream
            # will already have been exhausted.
            # 如果解析器中存在能够直接解析请求内容实体的解析器，则直接返回请求实体
            if self._supports_form_parsing():
                return (self._request.POST, self._request.FILES)
            stream = None

        # 如果数据流和媒体类型中有任何一个不存在则返回一个
        # (QueryDict, MultiValueDict)形式的元祖。
        if stream is None or media_type is None:
            if media_type and is_form_media_type(media_type):
                empty_data = QueryDict('', encoding=self._request._encoding)
            else:
                empty_data = {}
            empty_files = MultiValueDict()
            return (empty_data, empty_files)

        # 调用协调器选择合适的解析器
        parser = self.negotiator.select_parser(self, self.parsers)

        # 不存在用于解析的解析器直接raise一个错误
        if not parser:
            raise exceptions.UnsupportedMediaType(media_type)

        try:
            # 使用指定的解析器对于内容进行解析，解析过程中如果报错则raise错误
            parsed = parser.parse(stream, media_type, self.parser_context)
        except:
            # If we get an exception during parsing, fill in empty data and
            # re-raise.  Ensures we don't simply repeat the error when
            # attempting to render the browsable renderer response, or when
            # logging the request or similar.
            self._data = QueryDict('', encoding=self._request._encoding)
            self._files = MultiValueDict()
            self._full_data = self._data
            raise

        # Parser classes may return the raw data, or a
        # DataAndFiles object.  Unpack the result as required.
        # 返回解析后的文本内容和文件内容，如果出现文件属性不存在的报错，讲文件属性设置为
        # 一个MultiValueDict类
        try:
            return (parsed.data, parsed.files)
        except AttributeError:
            empty_files = MultiValueDict()
            return (parsed, empty_files)

    def _authenticate(self):
        """
        Attempt to authenticate the request using each authentication instance
        in turn.
        迭代类的认证器对请求进行认证，认证成功则返回用户以及认证信息，否则调用另外一个用于匿名
        用户认证的方法
        """
        for authenticator in self.authenticators:
            try:
                user_auth_tuple = authenticator.authenticate(self)
            except exceptions.APIException:
                self._not_authenticated()
                raise

            if user_auth_tuple is not None:
                self._authenticator = authenticator
                self.user, self.auth = user_auth_tuple
                return

        self._not_authenticated()

    def _not_authenticated(self):
        """
        Set authenticator, user & authtoken representing an unauthenticated request.

        Defaults are None, AnonymousUser & None.
        用于认证匿名用户，后台设置中如果存在用户匿名认证的属性则应用上来，否则该匿名用户的
        用户属性和认证属性将被定义为None
        """
        self._authenticator = None

        if api_settings.UNAUTHENTICATED_USER:
            self.user = api_settings.UNAUTHENTICATED_USER()
        else:
            self.user = None

        if api_settings.UNAUTHENTICATED_TOKEN:
            self.auth = api_settings.UNAUTHENTICATED_TOKEN()
        else:
            self.auth = None

    def __getattribute__(self, attr):
        """
        If an attribute does not exist on this instance, then we also attempt
        to proxy it to the underlying HttpRequest object.
        调用父类的查找属性的方法，出现调用HttpRequest类的获取属性的方法，否则报错
        """
        try:
            return super(Request, self).__getattribute__(attr)
        except AttributeError:
            info = sys.exc_info()
            try:
                return getattr(self._request, attr)
            except AttributeError:
                six.reraise(info[0], info[1], info[2].tb_next)

    @property
    def DATA(self):
        raise NotImplementedError(
            '`request.DATA` has been deprecated in favor of `request.data` '
            'since version 3.0, and has been fully removed as of version 3.2.'
        )

    @property
    def POST(self):
        """
        对request.POST属性进行初始化
        """
        # Ensure that request.POST uses our request parsing.
        if not _hasattr(self, '_data'):
            self._load_data_and_files()
        if is_form_media_type(self.content_type):
            return self._data
        return QueryDict('', encoding=self._request._encoding)

    @property
    def FILES(self):
        """
        初始化request.FILES
        """
        # Leave this one alone for backwards compat with Django's request.FILES
        # Different from the other two cases, which are not valid property
        # names on the WSGIRequest class.
        if not _hasattr(self, '_files'):
            self._load_data_and_files()
        return self._files

    @property
    def QUERY_PARAMS(self):
        raise NotImplementedError(
            '`request.QUERY_PARAMS` has been deprecated in favor of `request.query_params` '
            'since version 3.0, and has been fully removed as of version 3.2.'
        )

    def force_plaintext_errors(self, value):
        # Hack to allow our exception handler to force choice of
        # plaintext or html error responses.
        self._request.is_ajax = lambda: value
