# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.v1alpha1_plugin import V1alpha1Plugin  # noqa: E501
from openapi_client.rest import ApiException

class TestV1alpha1Plugin(unittest.TestCase):
    """V1alpha1Plugin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1Plugin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1alpha1_plugin.V1alpha1Plugin()  # noqa: E501
        if include_optional :
            return V1alpha1Plugin(
                build_source = '0', 
                build_version = '0', 
                category = '0', 
                code_repo = '0', 
                config_groups = [
                    openapi_client.models.v1alpha1/plugin_config_group.v1alpha1.PluginConfigGroup(
                        build_version = '0', 
                        config_name = '0', 
                        injection = '0', 
                        options = [
                            openapi_client.models.v1alpha1/plugin_config_group_option.v1alpha1.PluginConfigGroupOption(
                                attr_alt_value = '0', 
                                attr_default_value = '0', 
                                attr_info = '0', 
                                attr_name = '0', 
                                attr_type = '0', 
                                build_version = '0', 
                                is_change = True, 
                                plugin_id = '0', 
                                protocol = '0', 
                                service_meta_type = '0', )
                            ], 
                        plugin_id = '0', 
                        service_meta_type = '0', )
                    ], 
                create_time = '0', 
                desc = '0', 
                image = '0', 
                origin = '0', 
                origin_share_id = '0', 
                plugin_alias = '0', 
                plugin_id = '0', 
                plugin_image = openapi_client.models.v1alpha1/image_info.v1alpha1.ImageInfo(
                    hub_password = '0', 
                    hub_url = '0', 
                    hub_user = '0', 
                    is_trust = True, 
                    namespace = '0', ), 
                plugin_key = '0', 
                plugin_name = '0', 
                share_image = '0'
            )
        else :
            return V1alpha1Plugin(
                build_source = '0',
                build_version = '0',
                category = '0',
                code_repo = '0',
                create_time = '0',
                desc = '0',
                image = '0',
                origin = '0',
                origin_share_id = '0',
                plugin_alias = '0',
                plugin_id = '0',
                plugin_image = openapi_client.models.v1alpha1/image_info.v1alpha1.ImageInfo(
                    hub_password = '0', 
                    hub_url = '0', 
                    hub_user = '0', 
                    is_trust = True, 
                    namespace = '0', ),
                plugin_key = '0',
                plugin_name = '0',
                share_image = '0',
        )

    def testV1alpha1Plugin(self):
        """Test V1alpha1Plugin"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()