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


class V1alpha1PluginConfigGroup(object):
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
        'build_version': 'str',
        'config_name': 'str',
        'injection': 'str',
        'options': 'list[V1alpha1PluginConfigGroupOption]',
        'plugin_id': 'str',
        'service_meta_type': 'str'
    }

    attribute_map = {
        'build_version': 'build_version',
        'config_name': 'config_name',
        'injection': 'injection',
        'options': 'options',
        'plugin_id': 'plugin_id',
        'service_meta_type': 'service_meta_type'
    }

    def __init__(self, build_version=None, config_name=None, injection=None, options=None, plugin_id=None, service_meta_type=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1PluginConfigGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._build_version = None
        self._config_name = None
        self._injection = None
        self._options = None
        self._plugin_id = None
        self._service_meta_type = None
        self.discriminator = None

        self.build_version = build_version
        self.config_name = config_name
        self.injection = injection
        if options is not None:
            self.options = options
        self.plugin_id = plugin_id
        self.service_meta_type = service_meta_type

    @property
    def build_version(self):
        """Gets the build_version of this V1alpha1PluginConfigGroup.  # noqa: E501


        :return: The build_version of this V1alpha1PluginConfigGroup.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this V1alpha1PluginConfigGroup.


        :param build_version: The build_version of this V1alpha1PluginConfigGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and build_version is None:  # noqa: E501
            raise ValueError("Invalid value for `build_version`, must not be `None`")  # noqa: E501

        self._build_version = build_version

    @property
    def config_name(self):
        """Gets the config_name of this V1alpha1PluginConfigGroup.  # noqa: E501


        :return: The config_name of this V1alpha1PluginConfigGroup.  # noqa: E501
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this V1alpha1PluginConfigGroup.


        :param config_name: The config_name of this V1alpha1PluginConfigGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and config_name is None:  # noqa: E501
            raise ValueError("Invalid value for `config_name`, must not be `None`")  # noqa: E501

        self._config_name = config_name

    @property
    def injection(self):
        """Gets the injection of this V1alpha1PluginConfigGroup.  # noqa: E501


        :return: The injection of this V1alpha1PluginConfigGroup.  # noqa: E501
        :rtype: str
        """
        return self._injection

    @injection.setter
    def injection(self, injection):
        """Sets the injection of this V1alpha1PluginConfigGroup.


        :param injection: The injection of this V1alpha1PluginConfigGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and injection is None:  # noqa: E501
            raise ValueError("Invalid value for `injection`, must not be `None`")  # noqa: E501

        self._injection = injection

    @property
    def options(self):
        """Gets the options of this V1alpha1PluginConfigGroup.  # noqa: E501


        :return: The options of this V1alpha1PluginConfigGroup.  # noqa: E501
        :rtype: list[V1alpha1PluginConfigGroupOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this V1alpha1PluginConfigGroup.


        :param options: The options of this V1alpha1PluginConfigGroup.  # noqa: E501
        :type: list[V1alpha1PluginConfigGroupOption]
        """

        self._options = options

    @property
    def plugin_id(self):
        """Gets the plugin_id of this V1alpha1PluginConfigGroup.  # noqa: E501


        :return: The plugin_id of this V1alpha1PluginConfigGroup.  # noqa: E501
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this V1alpha1PluginConfigGroup.


        :param plugin_id: The plugin_id of this V1alpha1PluginConfigGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_id is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_id`, must not be `None`")  # noqa: E501

        self._plugin_id = plugin_id

    @property
    def service_meta_type(self):
        """Gets the service_meta_type of this V1alpha1PluginConfigGroup.  # noqa: E501


        :return: The service_meta_type of this V1alpha1PluginConfigGroup.  # noqa: E501
        :rtype: str
        """
        return self._service_meta_type

    @service_meta_type.setter
    def service_meta_type(self, service_meta_type):
        """Sets the service_meta_type of this V1alpha1PluginConfigGroup.


        :param service_meta_type: The service_meta_type of this V1alpha1PluginConfigGroup.  # noqa: E501
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
        if not isinstance(other, V1alpha1PluginConfigGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1PluginConfigGroup):
            return True

        return self.to_dict() != other.to_dict()