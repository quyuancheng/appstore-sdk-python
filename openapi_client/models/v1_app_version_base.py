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


class V1AppVersionBase(object):
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
        'app_key_id': 'str',
        'app_version': 'str',
        'app_version_alias': 'str',
        'create_time': 'datetime',
        'delivery_mode': 'str',
        'desc': 'str',
        'enable': 'bool',
        'is_plugin': 'bool',
        'rainbond_version': 'str',
        'update_time': 'datetime',
        'update_version': 'int'
    }

    attribute_map = {
        'app_key_id': 'appKeyID',
        'app_version': 'appVersion',
        'app_version_alias': 'appVersionAlias',
        'create_time': 'createTime',
        'delivery_mode': 'deliveryMode',
        'desc': 'desc',
        'enable': 'enable',
        'is_plugin': 'is_plugin',
        'rainbond_version': 'rainbondVersion',
        'update_time': 'updateTime',
        'update_version': 'updateVersion'
    }

    def __init__(self, app_key_id=None, app_version=None, app_version_alias=None, create_time=None, delivery_mode=None, desc=None, enable=None, is_plugin=None, rainbond_version=None, update_time=None, update_version=None, local_vars_configuration=None):  # noqa: E501
        """V1AppVersionBase - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_key_id = None
        self._app_version = None
        self._app_version_alias = None
        self._create_time = None
        self._delivery_mode = None
        self._desc = None
        self._enable = None
        self._is_plugin = None
        self._rainbond_version = None
        self._update_time = None
        self._update_version = None
        self.discriminator = None

        self.app_key_id = app_key_id
        self.app_version = app_version
        self.app_version_alias = app_version_alias
        self.create_time = create_time
        self.delivery_mode = delivery_mode
        self.desc = desc
        self.enable = enable
        self.is_plugin = is_plugin
        self.rainbond_version = rainbond_version
        self.update_time = update_time
        self.update_version = update_version

    @property
    def app_key_id(self):
        """Gets the app_key_id of this V1AppVersionBase.  # noqa: E501

        应用 ID  # noqa: E501

        :return: The app_key_id of this V1AppVersionBase.  # noqa: E501
        :rtype: str
        """
        return self._app_key_id

    @app_key_id.setter
    def app_key_id(self, app_key_id):
        """Sets the app_key_id of this V1AppVersionBase.

        应用 ID  # noqa: E501

        :param app_key_id: The app_key_id of this V1AppVersionBase.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_key_id`, must not be `None`")  # noqa: E501

        self._app_key_id = app_key_id

    @property
    def app_version(self):
        """Gets the app_version of this V1AppVersionBase.  # noqa: E501

        应用版本  # noqa: E501

        :return: The app_version of this V1AppVersionBase.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this V1AppVersionBase.

        应用版本  # noqa: E501

        :param app_version: The app_version of this V1AppVersionBase.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_version is None:  # noqa: E501
            raise ValueError("Invalid value for `app_version`, must not be `None`")  # noqa: E501

        self._app_version = app_version

    @property
    def app_version_alias(self):
        """Gets the app_version_alias of this V1AppVersionBase.  # noqa: E501

        版本别名  # noqa: E501

        :return: The app_version_alias of this V1AppVersionBase.  # noqa: E501
        :rtype: str
        """
        return self._app_version_alias

    @app_version_alias.setter
    def app_version_alias(self, app_version_alias):
        """Sets the app_version_alias of this V1AppVersionBase.

        版本别名  # noqa: E501

        :param app_version_alias: The app_version_alias of this V1AppVersionBase.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_version_alias is None:  # noqa: E501
            raise ValueError("Invalid value for `app_version_alias`, must not be `None`")  # noqa: E501

        self._app_version_alias = app_version_alias

    @property
    def create_time(self):
        """Gets the create_time of this V1AppVersionBase.  # noqa: E501

        创建时间  # noqa: E501

        :return: The create_time of this V1AppVersionBase.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1AppVersionBase.

        创建时间  # noqa: E501

        :param create_time: The create_time of this V1AppVersionBase.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def delivery_mode(self):
        """Gets the delivery_mode of this V1AppVersionBase.  # noqa: E501

        交付模式  # noqa: E501

        :return: The delivery_mode of this V1AppVersionBase.  # noqa: E501
        :rtype: str
        """
        return self._delivery_mode

    @delivery_mode.setter
    def delivery_mode(self, delivery_mode):
        """Sets the delivery_mode of this V1AppVersionBase.

        交付模式  # noqa: E501

        :param delivery_mode: The delivery_mode of this V1AppVersionBase.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and delivery_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `delivery_mode`, must not be `None`")  # noqa: E501

        self._delivery_mode = delivery_mode

    @property
    def desc(self):
        """Gets the desc of this V1AppVersionBase.  # noqa: E501

        描述  # noqa: E501

        :return: The desc of this V1AppVersionBase.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this V1AppVersionBase.

        描述  # noqa: E501

        :param desc: The desc of this V1AppVersionBase.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and desc is None:  # noqa: E501
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501

        self._desc = desc

    @property
    def enable(self):
        """Gets the enable of this V1AppVersionBase.  # noqa: E501

        开启  # noqa: E501

        :return: The enable of this V1AppVersionBase.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this V1AppVersionBase.

        开启  # noqa: E501

        :param enable: The enable of this V1AppVersionBase.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable is None:  # noqa: E501
            raise ValueError("Invalid value for `enable`, must not be `None`")  # noqa: E501

        self._enable = enable

    @property
    def is_plugin(self):
        """Gets the is_plugin of this V1AppVersionBase.  # noqa: E501

        是否作为插件  # noqa: E501

        :return: The is_plugin of this V1AppVersionBase.  # noqa: E501
        :rtype: bool
        """
        return self._is_plugin

    @is_plugin.setter
    def is_plugin(self, is_plugin):
        """Sets the is_plugin of this V1AppVersionBase.

        是否作为插件  # noqa: E501

        :param is_plugin: The is_plugin of this V1AppVersionBase.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_plugin is None:  # noqa: E501
            raise ValueError("Invalid value for `is_plugin`, must not be `None`")  # noqa: E501

        self._is_plugin = is_plugin

    @property
    def rainbond_version(self):
        """Gets the rainbond_version of this V1AppVersionBase.  # noqa: E501

        rainbond 版本  # noqa: E501

        :return: The rainbond_version of this V1AppVersionBase.  # noqa: E501
        :rtype: str
        """
        return self._rainbond_version

    @rainbond_version.setter
    def rainbond_version(self, rainbond_version):
        """Sets the rainbond_version of this V1AppVersionBase.

        rainbond 版本  # noqa: E501

        :param rainbond_version: The rainbond_version of this V1AppVersionBase.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rainbond_version is None:  # noqa: E501
            raise ValueError("Invalid value for `rainbond_version`, must not be `None`")  # noqa: E501

        self._rainbond_version = rainbond_version

    @property
    def update_time(self):
        """Gets the update_time of this V1AppVersionBase.  # noqa: E501

        更新时间  # noqa: E501

        :return: The update_time of this V1AppVersionBase.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this V1AppVersionBase.

        更新时间  # noqa: E501

        :param update_time: The update_time of this V1AppVersionBase.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def update_version(self):
        """Gets the update_version of this V1AppVersionBase.  # noqa: E501

        升级版本  # noqa: E501

        :return: The update_version of this V1AppVersionBase.  # noqa: E501
        :rtype: int
        """
        return self._update_version

    @update_version.setter
    def update_version(self, update_version):
        """Sets the update_version of this V1AppVersionBase.

        升级版本  # noqa: E501

        :param update_version: The update_version of this V1AppVersionBase.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and update_version is None:  # noqa: E501
            raise ValueError("Invalid value for `update_version`, must not be `None`")  # noqa: E501

        self._update_version = update_version

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
        if not isinstance(other, V1AppVersionBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AppVersionBase):
            return True

        return self.to_dict() != other.to_dict()
