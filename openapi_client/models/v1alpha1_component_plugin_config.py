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


class V1alpha1ComponentPluginConfig(object):
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
        'attr': 'list[object]',
        'build_version': 'str',
        'cpu_required': 'int',
        'create_time': 'str',
        'memory_required': 'int',
        'plugin_id': 'str',
        'plugin_key': 'str',
        'plugin_status': 'bool',
        'service_id': 'str',
        'service_meta_type': 'str'
    }

    attribute_map = {
        'attr': 'attr',
        'build_version': 'build_version',
        'cpu_required': 'cpu_required',
        'create_time': 'create_time',
        'memory_required': 'memory_required',
        'plugin_id': 'plugin_id',
        'plugin_key': 'plugin_key',
        'plugin_status': 'plugin_status',
        'service_id': 'service_id',
        'service_meta_type': 'service_meta_type'
    }

    def __init__(self, attr=None, build_version=None, cpu_required=None, create_time=None, memory_required=None, plugin_id=None, plugin_key=None, plugin_status=None, service_id=None, service_meta_type=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ComponentPluginConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attr = None
        self._build_version = None
        self._cpu_required = None
        self._create_time = None
        self._memory_required = None
        self._plugin_id = None
        self._plugin_key = None
        self._plugin_status = None
        self._service_id = None
        self._service_meta_type = None
        self.discriminator = None

        self.attr = attr
        self.build_version = build_version
        self.cpu_required = cpu_required
        self.create_time = create_time
        self.memory_required = memory_required
        self.plugin_id = plugin_id
        self.plugin_key = plugin_key
        self.plugin_status = plugin_status
        self.service_id = service_id
        self.service_meta_type = service_meta_type

    @property
    def attr(self):
        """Gets the attr of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The attr of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: list[object]
        """
        return self._attr

    @attr.setter
    def attr(self, attr):
        """Sets the attr of this V1alpha1ComponentPluginConfig.


        :param attr: The attr of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and attr is None:  # noqa: E501
            raise ValueError("Invalid value for `attr`, must not be `None`")  # noqa: E501

        self._attr = attr

    @property
    def build_version(self):
        """Gets the build_version of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The build_version of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this V1alpha1ComponentPluginConfig.


        :param build_version: The build_version of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and build_version is None:  # noqa: E501
            raise ValueError("Invalid value for `build_version`, must not be `None`")  # noqa: E501

        self._build_version = build_version

    @property
    def cpu_required(self):
        """Gets the cpu_required of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The cpu_required of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: int
        """
        return self._cpu_required

    @cpu_required.setter
    def cpu_required(self, cpu_required):
        """Sets the cpu_required of this V1alpha1ComponentPluginConfig.


        :param cpu_required: The cpu_required of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and cpu_required is None:  # noqa: E501
            raise ValueError("Invalid value for `cpu_required`, must not be `None`")  # noqa: E501

        self._cpu_required = cpu_required

    @property
    def create_time(self):
        """Gets the create_time of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The create_time of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1alpha1ComponentPluginConfig.


        :param create_time: The create_time of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def memory_required(self):
        """Gets the memory_required of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The memory_required of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: int
        """
        return self._memory_required

    @memory_required.setter
    def memory_required(self, memory_required):
        """Sets the memory_required of this V1alpha1ComponentPluginConfig.


        :param memory_required: The memory_required of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and memory_required is None:  # noqa: E501
            raise ValueError("Invalid value for `memory_required`, must not be `None`")  # noqa: E501

        self._memory_required = memory_required

    @property
    def plugin_id(self):
        """Gets the plugin_id of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The plugin_id of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this V1alpha1ComponentPluginConfig.


        :param plugin_id: The plugin_id of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_id is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_id`, must not be `None`")  # noqa: E501

        self._plugin_id = plugin_id

    @property
    def plugin_key(self):
        """Gets the plugin_key of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The plugin_key of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._plugin_key

    @plugin_key.setter
    def plugin_key(self, plugin_key):
        """Sets the plugin_key of this V1alpha1ComponentPluginConfig.


        :param plugin_key: The plugin_key of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_key is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_key`, must not be `None`")  # noqa: E501

        self._plugin_key = plugin_key

    @property
    def plugin_status(self):
        """Gets the plugin_status of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The plugin_status of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: bool
        """
        return self._plugin_status

    @plugin_status.setter
    def plugin_status(self, plugin_status):
        """Sets the plugin_status of this V1alpha1ComponentPluginConfig.


        :param plugin_status: The plugin_status of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and plugin_status is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_status`, must not be `None`")  # noqa: E501

        self._plugin_status = plugin_status

    @property
    def service_id(self):
        """Gets the service_id of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The service_id of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this V1alpha1ComponentPluginConfig.


        :param service_id: The service_id of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service_id is None:  # noqa: E501
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

    @property
    def service_meta_type(self):
        """Gets the service_meta_type of this V1alpha1ComponentPluginConfig.  # noqa: E501


        :return: The service_meta_type of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._service_meta_type

    @service_meta_type.setter
    def service_meta_type(self, service_meta_type):
        """Sets the service_meta_type of this V1alpha1ComponentPluginConfig.


        :param service_meta_type: The service_meta_type of this V1alpha1ComponentPluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service_meta_type is None:  # noqa: E501
            raise ValueError("Invalid value for `service_meta_type`, must not be `None`")  # noqa: E501

        self._service_meta_type = service_meta_type

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
        if not isinstance(other, V1alpha1ComponentPluginConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ComponentPluginConfig):
            return True

        return self.to_dict() != other.to_dict()