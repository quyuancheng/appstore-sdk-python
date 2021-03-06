# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: huangrh@goodrain.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class V1alpha1IngressSreamRoute(object):
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
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'component_key': 'component_key',
        'connection_timeout': 'connection_timeout',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, component_key=None, connection_timeout=None, port=None, protocol=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1IngressSreamRoute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._component_key = None
        self._connection_timeout = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        self.component_key = component_key
        self.connection_timeout = connection_timeout
        self.port = port
        self.protocol = protocol

    @property
    def component_key(self):
        """Gets the component_key of this V1alpha1IngressSreamRoute.  # noqa: E501


        :return: The component_key of this V1alpha1IngressSreamRoute.  # noqa: E501
        :rtype: str
        """
        return self._component_key

    @component_key.setter
    def component_key(self, component_key):
        """Sets the component_key of this V1alpha1IngressSreamRoute.


        :param component_key: The component_key of this V1alpha1IngressSreamRoute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and component_key is None:  # noqa: E501
            raise ValueError("Invalid value for `component_key`, must not be `None`")  # noqa: E501

        self._component_key = component_key

    @property
    def connection_timeout(self):
        """Gets the connection_timeout of this V1alpha1IngressSreamRoute.  # noqa: E501


        :return: The connection_timeout of this V1alpha1IngressSreamRoute.  # noqa: E501
        :rtype: int
        """
        return self._connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, connection_timeout):
        """Sets the connection_timeout of this V1alpha1IngressSreamRoute.


        :param connection_timeout: The connection_timeout of this V1alpha1IngressSreamRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and connection_timeout is None:  # noqa: E501
            raise ValueError("Invalid value for `connection_timeout`, must not be `None`")  # noqa: E501

        self._connection_timeout = connection_timeout

    @property
    def port(self):
        """Gets the port of this V1alpha1IngressSreamRoute.  # noqa: E501


        :return: The port of this V1alpha1IngressSreamRoute.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this V1alpha1IngressSreamRoute.


        :param port: The port of this V1alpha1IngressSreamRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this V1alpha1IngressSreamRoute.  # noqa: E501


        :return: The protocol of this V1alpha1IngressSreamRoute.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this V1alpha1IngressSreamRoute.


        :param protocol: The protocol of this V1alpha1IngressSreamRoute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

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
        if not isinstance(other, V1alpha1IngressSreamRoute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1IngressSreamRoute):
            return True

        return self.to_dict() != other.to_dict()
