# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: huangrh@goodrain.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.v1alpha1_plugin_config_group_option import V1alpha1PluginConfigGroupOption  # noqa: E501
from openapi_client.rest import ApiException

class TestV1alpha1PluginConfigGroupOption(unittest.TestCase):
    """V1alpha1PluginConfigGroupOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1PluginConfigGroupOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1alpha1_plugin_config_group_option.V1alpha1PluginConfigGroupOption()  # noqa: E501
        if include_optional :
            return V1alpha1PluginConfigGroupOption(
                id = 56, 
                attr_alt_value = '0', 
                attr_default_value = '0', 
                attr_info = '0', 
                attr_name = '0', 
                attr_type = '0', 
                build_version = '0', 
                is_change = True, 
                plugin_id = '0', 
                protocol = '0', 
                service_meta_type = '0'
            )
        else :
            return V1alpha1PluginConfigGroupOption(
                id = 56,
                attr_alt_value = '0',
                attr_default_value = '0',
                attr_info = '0',
                attr_name = '0',
                attr_type = '0',
                build_version = '0',
                is_change = True,
                plugin_id = '0',
                protocol = '0',
                service_meta_type = '0',
        )

    def testV1alpha1PluginConfigGroupOption(self):
        """Test V1alpha1PluginConfigGroupOption"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
