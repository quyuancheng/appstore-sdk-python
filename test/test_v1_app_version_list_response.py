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
from openapi_client.models.v1_app_version_list_response import V1AppVersionListResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestV1AppVersionListResponse(unittest.TestCase):
    """V1AppVersionListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1AppVersionListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1_app_version_list_response.V1AppVersionListResponse()  # noqa: E501
        if include_optional :
            return V1AppVersionListResponse(
                versions = [
                    openapi_client.models.v1/app_version_base.v1.AppVersionBase(
                        app_key_id = '0', 
                        app_version = '0', 
                        app_version_alias = '0', 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        delivery_mode = '0', 
                        desc = '0', 
                        enable = True, 
                        rainbond_version = '0', 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_version = 56, )
                    ]
            )
        else :
            return V1AppVersionListResponse(
                versions = [
                    openapi_client.models.v1/app_version_base.v1.AppVersionBase(
                        app_key_id = '0', 
                        app_version = '0', 
                        app_version_alias = '0', 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        delivery_mode = '0', 
                        desc = '0', 
                        enable = True, 
                        rainbond_version = '0', 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_version = 56, )
                    ],
        )

    def testV1AppVersionListResponse(self):
        """Test V1AppVersionListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
