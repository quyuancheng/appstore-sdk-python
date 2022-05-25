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
from openapi_client.models.v1alpha1_component_graph import V1alpha1ComponentGraph  # noqa: E501
from openapi_client.rest import ApiException

class TestV1alpha1ComponentGraph(unittest.TestCase):
    """V1alpha1ComponentGraph unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ComponentGraph
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1alpha1_component_graph.V1alpha1ComponentGraph()  # noqa: E501
        if include_optional :
            return V1alpha1ComponentGraph(
                component_id = '0', 
                graph_id = '0', 
                promql = '0', 
                sequence = 56, 
                title = '0'
            )
        else :
            return V1alpha1ComponentGraph(
                component_id = '0',
                graph_id = '0',
                promql = '0',
                sequence = 56,
                title = '0',
        )

    def testV1alpha1ComponentGraph(self):
        """Test V1alpha1ComponentGraph"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
