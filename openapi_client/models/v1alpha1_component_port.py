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


class V1alpha1ComponentPort(object):
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
        'container_port': 'int',
        'is_inner_service': 'bool',
        'is_outer_service': 'bool',
        'port_alias': 'str',
        'protocol': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'container_port': 'container_port',
        'is_inner_service': 'is_inner_service',
        'is_outer_service': 'is_outer_service',
        'port_alias': 'port_alias',
        'protocol': 'protocol',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, container_port=None, is_inner_service=None, is_outer_service=None, port_alias=None, protocol=None, tenant_id=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ComponentPort - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container_port = None
        self._is_inner_service = None
        self._is_outer_service = None
        self._port_alias = None
        self._protocol = None
        self._tenant_id = None
        self.discriminator = None

        self.container_port = container_port
        self.is_inner_service = is_inner_service
        self.is_outer_service = is_outer_service
        self.port_alias = port_alias
        self.protocol = protocol
        self.tenant_id = tenant_id

    @property
    def container_port(self):
        """Gets the container_port of this V1alpha1ComponentPort.  # noqa: E501


        :return: The container_port of this V1alpha1ComponentPort.  # noqa: E501
        :rtype: int
        """
        return self._container_port

    @container_port.setter
    def container_port(self, container_port):
        """Sets the container_port of this V1alpha1ComponentPort.


        :param container_port: The container_port of this V1alpha1ComponentPort.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and container_port is None:  # noqa: E501
            raise ValueError("Invalid value for `container_port`, must not be `None`")  # noqa: E501

        self._container_port = container_port

    @property
    def is_inner_service(self):
        """Gets the is_inner_service of this V1alpha1ComponentPort.  # noqa: E501


        :return: The is_inner_service of this V1alpha1ComponentPort.  # noqa: E501
        :rtype: bool
        """
        return self._is_inner_service

    @is_inner_service.setter
    def is_inner_service(self, is_inner_service):
        """Sets the is_inner_service of this V1alpha1ComponentPort.


        :param is_inner_service: The is_inner_service of this V1alpha1ComponentPort.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_inner_service is None:  # noqa: E501
            raise ValueError("Invalid value for `is_inner_service`, must not be `None`")  # noqa: E501

        self._is_inner_service = is_inner_service

    @property
    def is_outer_service(self):
        """Gets the is_outer_service of this V1alpha1ComponentPort.  # noqa: E501


        :return: The is_outer_service of this V1alpha1ComponentPort.  # noqa: E501
        :rtype: bool
        """
        return self._is_outer_service

    @is_outer_service.setter
    def is_outer_service(self, is_outer_service):
        """Sets the is_outer_service of this V1alpha1ComponentPort.


        :param is_outer_service: The is_outer_service of this V1alpha1ComponentPort.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_outer_service is None:  # noqa: E501
            raise ValueError("Invalid value for `is_outer_service`, must not be `None`")  # noqa: E501

        self._is_outer_service = is_outer_service

    @property
    def port_alias(self):
        """Gets the port_alias of this V1alpha1ComponentPort.  # noqa: E501


        :return: The port_alias of this V1alpha1ComponentPort.  # noqa: E501
        :rtype: str
        """
        return self._port_alias

    @port_alias.setter
    def port_alias(self, port_alias):
        """Sets the port_alias of this V1alpha1ComponentPort.


        :param port_alias: The port_alias of this V1alpha1ComponentPort.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and port_alias is None:  # noqa: E501
            raise ValueError("Invalid value for `port_alias`, must not be `None`")  # noqa: E501

        self._port_alias = port_alias

    @property
    def protocol(self):
        """Gets the protocol of this V1alpha1ComponentPort.  # noqa: E501


        :return: The protocol of this V1alpha1ComponentPort.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this V1alpha1ComponentPort.


        :param protocol: The protocol of this V1alpha1ComponentPort.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def tenant_id(self):
        """Gets the tenant_id of this V1alpha1ComponentPort.  # noqa: E501


        :return: The tenant_id of this V1alpha1ComponentPort.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this V1alpha1ComponentPort.


        :param tenant_id: The tenant_id of this V1alpha1ComponentPort.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

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
        if not isinstance(other, V1alpha1ComponentPort):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ComponentPort):
            return True

        return self.to_dict() != other.to_dict()
