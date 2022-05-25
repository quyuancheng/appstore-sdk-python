# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class V1alpha1IngressHTTPRoute(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'component_key': 'str',
        'connection_timeout': 'int',
        'cookies': 'dict(str, str)',
        'default_domain': 'bool',
        'headers': 'dict(str, str)',
        'load_balancing': 'str',
        'location': 'str',
        'port': 'int',
        'proxy_buffer': 'bool',
        'proxy_buffer_numbers': 'int',
        'proxy_buffer_size': 'int',
        'proxy_header': 'dict(str, str)',
        'request_body_size_limit': 'int',
        'request_timeout': 'int',
        'response_timeout': 'int',
        'ssl': 'bool',
        'websocket': 'bool'
    }

    attribute_map = {
        'component_key': 'component_key',
        'connection_timeout': 'connection_timeout',
        'cookies': 'cookies',
        'default_domain': 'default_domain',
        'headers': 'headers',
        'load_balancing': 'load_balancing',
        'location': 'location',
        'port': 'port',
        'proxy_buffer': 'proxy_buffer',
        'proxy_buffer_numbers': 'proxy_buffer_numbers',
        'proxy_buffer_size': 'proxy_buffer_size',
        'proxy_header': 'proxy_header',
        'request_body_size_limit': 'request_body_size_limit',
        'request_timeout': 'request_timeout',
        'response_timeout': 'response_timeout',
        'ssl': 'ssl',
        'websocket': 'websocket'
    }

    def __init__(self, component_key=None, connection_timeout=None, cookies=None, default_domain=None, headers=None, load_balancing=None, location=None, port=None, proxy_buffer=None, proxy_buffer_numbers=None, proxy_buffer_size=None, proxy_header=None, request_body_size_limit=None, request_timeout=None, response_timeout=None, ssl=None, websocket=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1IngressHTTPRoute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._component_key = None
        self._connection_timeout = None
        self._cookies = None
        self._default_domain = None
        self._headers = None
        self._load_balancing = None
        self._location = None
        self._port = None
        self._proxy_buffer = None
        self._proxy_buffer_numbers = None
        self._proxy_buffer_size = None
        self._proxy_header = None
        self._request_body_size_limit = None
        self._request_timeout = None
        self._response_timeout = None
        self._ssl = None
        self._websocket = None
        self.discriminator = None

        self.component_key = component_key
        self.connection_timeout = connection_timeout
        self.cookies = cookies
        self.default_domain = default_domain
        self.headers = headers
        self.load_balancing = load_balancing
        self.location = location
        self.port = port
        self.proxy_buffer = proxy_buffer
        self.proxy_buffer_numbers = proxy_buffer_numbers
        self.proxy_buffer_size = proxy_buffer_size
        self.proxy_header = proxy_header
        self.request_body_size_limit = request_body_size_limit
        self.request_timeout = request_timeout
        self.response_timeout = response_timeout
        self.ssl = ssl
        self.websocket = websocket

    @property
    def component_key(self):
        """Gets the component_key of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The component_key of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: str
        """
        return self._component_key

    @component_key.setter
    def component_key(self, component_key):
        """Sets the component_key of this V1alpha1IngressHTTPRoute.


        :param component_key: The component_key of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and component_key is None:  # noqa: E501
            raise ValueError("Invalid value for `component_key`, must not be `None`")  # noqa: E501

        self._component_key = component_key

    @property
    def connection_timeout(self):
        """Gets the connection_timeout of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The connection_timeout of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: int
        """
        return self._connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, connection_timeout):
        """Sets the connection_timeout of this V1alpha1IngressHTTPRoute.


        :param connection_timeout: The connection_timeout of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and connection_timeout is None:  # noqa: E501
            raise ValueError("Invalid value for `connection_timeout`, must not be `None`")  # noqa: E501

        self._connection_timeout = connection_timeout

    @property
    def cookies(self):
        """Gets the cookies of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The cookies of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        """Sets the cookies of this V1alpha1IngressHTTPRoute.


        :param cookies: The cookies of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and cookies is None:  # noqa: E501
            raise ValueError("Invalid value for `cookies`, must not be `None`")  # noqa: E501

        self._cookies = cookies

    @property
    def default_domain(self):
        """Gets the default_domain of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The default_domain of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: bool
        """
        return self._default_domain

    @default_domain.setter
    def default_domain(self, default_domain):
        """Sets the default_domain of this V1alpha1IngressHTTPRoute.


        :param default_domain: The default_domain of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and default_domain is None:  # noqa: E501
            raise ValueError("Invalid value for `default_domain`, must not be `None`")  # noqa: E501

        self._default_domain = default_domain

    @property
    def headers(self):
        """Gets the headers of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The headers of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this V1alpha1IngressHTTPRoute.


        :param headers: The headers of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and headers is None:  # noqa: E501
            raise ValueError("Invalid value for `headers`, must not be `None`")  # noqa: E501

        self._headers = headers

    @property
    def load_balancing(self):
        """Gets the load_balancing of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The load_balancing of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: str
        """
        return self._load_balancing

    @load_balancing.setter
    def load_balancing(self, load_balancing):
        """Sets the load_balancing of this V1alpha1IngressHTTPRoute.


        :param load_balancing: The load_balancing of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and load_balancing is None:  # noqa: E501
            raise ValueError("Invalid value for `load_balancing`, must not be `None`")  # noqa: E501

        self._load_balancing = load_balancing

    @property
    def location(self):
        """Gets the location of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The location of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this V1alpha1IngressHTTPRoute.


        :param location: The location of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def port(self):
        """Gets the port of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The port of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this V1alpha1IngressHTTPRoute.


        :param port: The port of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def proxy_buffer(self):
        """Gets the proxy_buffer of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The proxy_buffer of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: bool
        """
        return self._proxy_buffer

    @proxy_buffer.setter
    def proxy_buffer(self, proxy_buffer):
        """Sets the proxy_buffer of this V1alpha1IngressHTTPRoute.


        :param proxy_buffer: The proxy_buffer of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and proxy_buffer is None:  # noqa: E501
            raise ValueError("Invalid value for `proxy_buffer`, must not be `None`")  # noqa: E501

        self._proxy_buffer = proxy_buffer

    @property
    def proxy_buffer_numbers(self):
        """Gets the proxy_buffer_numbers of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The proxy_buffer_numbers of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: int
        """
        return self._proxy_buffer_numbers

    @proxy_buffer_numbers.setter
    def proxy_buffer_numbers(self, proxy_buffer_numbers):
        """Sets the proxy_buffer_numbers of this V1alpha1IngressHTTPRoute.


        :param proxy_buffer_numbers: The proxy_buffer_numbers of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and proxy_buffer_numbers is None:  # noqa: E501
            raise ValueError("Invalid value for `proxy_buffer_numbers`, must not be `None`")  # noqa: E501

        self._proxy_buffer_numbers = proxy_buffer_numbers

    @property
    def proxy_buffer_size(self):
        """Gets the proxy_buffer_size of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The proxy_buffer_size of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: int
        """
        return self._proxy_buffer_size

    @proxy_buffer_size.setter
    def proxy_buffer_size(self, proxy_buffer_size):
        """Sets the proxy_buffer_size of this V1alpha1IngressHTTPRoute.


        :param proxy_buffer_size: The proxy_buffer_size of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and proxy_buffer_size is None:  # noqa: E501
            raise ValueError("Invalid value for `proxy_buffer_size`, must not be `None`")  # noqa: E501

        self._proxy_buffer_size = proxy_buffer_size

    @property
    def proxy_header(self):
        """Gets the proxy_header of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The proxy_header of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._proxy_header

    @proxy_header.setter
    def proxy_header(self, proxy_header):
        """Sets the proxy_header of this V1alpha1IngressHTTPRoute.


        :param proxy_header: The proxy_header of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and proxy_header is None:  # noqa: E501
            raise ValueError("Invalid value for `proxy_header`, must not be `None`")  # noqa: E501

        self._proxy_header = proxy_header

    @property
    def request_body_size_limit(self):
        """Gets the request_body_size_limit of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The request_body_size_limit of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: int
        """
        return self._request_body_size_limit

    @request_body_size_limit.setter
    def request_body_size_limit(self, request_body_size_limit):
        """Sets the request_body_size_limit of this V1alpha1IngressHTTPRoute.


        :param request_body_size_limit: The request_body_size_limit of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and request_body_size_limit is None:  # noqa: E501
            raise ValueError("Invalid value for `request_body_size_limit`, must not be `None`")  # noqa: E501

        self._request_body_size_limit = request_body_size_limit

    @property
    def request_timeout(self):
        """Gets the request_timeout of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The request_timeout of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: int
        """
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, request_timeout):
        """Sets the request_timeout of this V1alpha1IngressHTTPRoute.


        :param request_timeout: The request_timeout of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and request_timeout is None:  # noqa: E501
            raise ValueError("Invalid value for `request_timeout`, must not be `None`")  # noqa: E501

        self._request_timeout = request_timeout

    @property
    def response_timeout(self):
        """Gets the response_timeout of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The response_timeout of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: int
        """
        return self._response_timeout

    @response_timeout.setter
    def response_timeout(self, response_timeout):
        """Sets the response_timeout of this V1alpha1IngressHTTPRoute.


        :param response_timeout: The response_timeout of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and response_timeout is None:  # noqa: E501
            raise ValueError("Invalid value for `response_timeout`, must not be `None`")  # noqa: E501

        self._response_timeout = response_timeout

    @property
    def ssl(self):
        """Gets the ssl of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The ssl of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this V1alpha1IngressHTTPRoute.


        :param ssl: The ssl of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and ssl is None:  # noqa: E501
            raise ValueError("Invalid value for `ssl`, must not be `None`")  # noqa: E501

        self._ssl = ssl

    @property
    def websocket(self):
        """Gets the websocket of this V1alpha1IngressHTTPRoute.  # noqa: E501


        :return: The websocket of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :rtype: bool
        """
        return self._websocket

    @websocket.setter
    def websocket(self, websocket):
        """Sets the websocket of this V1alpha1IngressHTTPRoute.


        :param websocket: The websocket of this V1alpha1IngressHTTPRoute.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and websocket is None:  # noqa: E501
            raise ValueError("Invalid value for `websocket`, must not be `None`")  # noqa: E501

        self._websocket = websocket

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1IngressHTTPRoute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1IngressHTTPRoute):
            return True

        return self.to_dict() != other.to_dict()
