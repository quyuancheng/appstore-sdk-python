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
from openapi_client.models.v1_create_app_paa_s_version_request import V1CreateAppPaaSVersionRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestV1CreateAppPaaSVersionRequest(unittest.TestCase):
    """V1CreateAppPaaSVersionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1CreateAppPaaSVersionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1_create_app_paa_s_version_request.V1CreateAppPaaSVersionRequest()  # noqa: E501
        if include_optional :
            return V1CreateAppPaaSVersionRequest(
                description = '0', 
                is_plugin = True, 
                rainbond_version = '0', 
                template = openapi_client.models.v1alpha1/rainbond_application_config.v1alpha1.RainbondApplicationConfig(
                    annotations = {
                        'key' : '0'
                        }, 
                    app_config_groups = [
                        openapi_client.models.v1alpha1/app_config_group.v1alpha1.AppConfigGroup(
                            component_ids = [
                                '0'
                                ], 
                            config_items = {
                                'key' : '0'
                                }, 
                            injection_type = '0', 
                            name = '0', )
                        ], 
                    apps = [
                        openapi_client.models.v1alpha1/component.v1alpha1.Component(
                            category = '0', 
                            cmd = '0', 
                            component_graphs = [
                                openapi_client.models.v1alpha1/component_graph.v1alpha1.ComponentGraph(
                                    component_id = '0', 
                                    graph_id = '0', 
                                    promql = '0', 
                                    sequence = 56, 
                                    title = '0', )
                                ], 
                            component_monitors = [
                                openapi_client.models.v1alpha1/component_monitor.v1alpha1.ComponentMonitor(
                                    interval = '0', 
                                    name = '0', 
                                    path = '0', 
                                    port = 56, 
                                    service_show_name = '0', )
                                ], 
                            cpu = 56, 
                            dep_service_map_list = [
                                openapi_client.models.v1alpha1/component_dep.v1alpha1.ComponentDep(
                                    dep_service_key = '0', )
                                ], 
                            deploy_version = '0', 
                            endpoints = openapi_client.models.v1alpha1/endpoints.v1alpha1.Endpoints(
                                endpoints_info = '0', 
                                endpoints_type = '0', 
                                service_cname = '0', ), 
                            extend_method = '0', 
                            extend_method_map = openapi_client.models.v1alpha1/component_extend_method_rule.v1alpha1.ComponentExtendMethodRule(
                                init_memory = 56, 
                                is_restart = 56, 
                                max_memory = 56, 
                                max_node = 56, 
                                min_memory = 56, 
                                min_node = 56, 
                                step_memory = 56, 
                                step_node = 56, ), 
                            image = '0', 
                            labels = {
                                'key' : '0'
                                }, 
                            language = '0', 
                            memory = 56, 
                            mnt_relation_list = [
                                openapi_client.models.v1alpha1/component_share_volume.v1alpha1.ComponentShareVolume(
                                    mnt_dir = '0', 
                                    mnt_name = '0', 
                                    service_share_uuid = '0', )
                                ], 
                            port_map_list = [
                                openapi_client.models.v1alpha1/component_port.v1alpha1.ComponentPort(
                                    container_port = 56, 
                                    is_inner_service = True, 
                                    is_outer_service = True, 
                                    port_alias = '0', 
                                    protocol = '0', 
                                    tenant_id = '0', )
                                ], 
                            probes = [
                                openapi_client.models.v1alpha1/component_probe.v1alpha1.ComponentProbe(
                                    id = 56, 
                                    cmd = '0', 
                                    failure_threshold = 56, 
                                    http_header = '0', 
                                    initial_delay_second = 56, 
                                    is_used = True, 
                                    mode = '0', 
                                    path = '0', 
                                    period_second = 56, 
                                    port = 56, 
                                    probe_id = '0', 
                                    scheme = '0', 
                                    service_id = '0', 
                                    success_threshold = 56, 
                                    timeout_second = 56, )
                                ], 
                            service_alias = '0', 
                            service_cname = '0', 
                            service_connect_info_map_list = [
                                openapi_client.models.v1alpha1/component_env.v1alpha1.ComponentEnv(
                                    attr_name = '0', 
                                    attr_value = '0', 
                                    container_port = 56, 
                                    is_change = True, 
                                    name = '0', )
                                ], 
                            service_env_map_list = [
                                openapi_client.models.v1alpha1/component_env.v1alpha1.ComponentEnv(
                                    attr_name = '0', 
                                    attr_value = '0', 
                                    container_port = 56, 
                                    is_change = True, 
                                    name = '0', )
                                ], 
                            service_id = '0', 
                            service_image = openapi_client.models.v1alpha1/image_info.v1alpha1.ImageInfo(
                                hub_password = '0', 
                                hub_url = '0', 
                                hub_user = '0', 
                                is_trust = True, 
                                namespace = '0', ), 
                            service_key = '0', 
                            service_name = '0', 
                            service_related_plugin_config = [
                                openapi_client.models.v1alpha1/component_plugin_config.v1alpha1.ComponentPluginConfig(
                                    attr = [
                                        openapi_client.models.v1alpha1/component_plugin_config/attr.v1alpha1.ComponentPluginConfig.attr()
                                        ], 
                                    build_version = '0', 
                                    cpu_required = 56, 
                                    create_time = '0', 
                                    memory_required = 56, 
                                    plugin_id = '0', 
                                    plugin_key = '0', 
                                    plugin_status = True, 
                                    service_id = '0', 
                                    service_meta_type = '0', )
                                ], 
                            service_share_uuid = '0', 
                            service_source = '0', 
                            service_type = '0', 
                            service_volume_map_list = [
                                openapi_client.models.v1alpha1/component_volume.v1alpha1.ComponentVolume(
                                    access_mode = '0', 
                                    file_content = '0', 
                                    mode = 56, 
                                    share_policy = '0', 
                                    volume_capacity = 56, 
                                    volume_name = '0', 
                                    volume_path = '0', 
                                    volume_type = '0', )
                                ], 
                            share_image = '0', 
                            share_type = '0', 
                            version = '0', )
                        ], 
                    group_key = '0', 
                    group_name = '0', 
                    group_version = '0', 
                    ingress_http_routes = [
                        openapi_client.models.v1alpha1/ingress_http_route.v1alpha1.IngressHTTPRoute(
                            component_key = '0', 
                            connection_timeout = 56, 
                            cookies = {
                                'key' : '0'
                                }, 
                            default_domain = True, 
                            headers = {
                                'key' : '0'
                                }, 
                            load_balancing = '0', 
                            location = '0', 
                            port = 56, 
                            proxy_buffer = True, 
                            proxy_buffer_numbers = 56, 
                            proxy_buffer_size = 56, 
                            proxy_header = {
                                'key' : '0'
                                }, 
                            request_body_size_limit = 56, 
                            request_timeout = 56, 
                            response_timeout = 56, 
                            ssl = True, 
                            websocket = True, )
                        ], 
                    ingress_stream_routes = [
                        openapi_client.models.v1alpha1/ingress_sream_route.v1alpha1.IngressSreamRoute(
                            component_key = '0', 
                            connection_timeout = 56, 
                            port = 56, 
                            protocol = '0', )
                        ], 
                    plugins = [
                        openapi_client.models.v1alpha1/plugin.v1alpha1.Plugin(
                            id = 56, 
                            build_source = '0', 
                            build_version = '0', 
                            category = '0', 
                            code_repo = '0', 
                            config_groups = [
                                openapi_client.models.v1alpha1/plugin_config_group.v1alpha1.PluginConfigGroup(
                                    id = 56, 
                                    build_version = '0', 
                                    config_name = '0', 
                                    injection = '0', 
                                    options = [
                                        openapi_client.models.v1alpha1/plugin_config_group_option.v1alpha1.PluginConfigGroupOption(
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
                            share_image = '0', )
                        ], 
                    template_version = '0', ), 
                template_type = '0', 
                version = '0', 
                version_alias = '0'
            )
        else :
            return V1CreateAppPaaSVersionRequest(
                description = '0',
                is_plugin = True,
                rainbond_version = '0',
                template = openapi_client.models.v1alpha1/rainbond_application_config.v1alpha1.RainbondApplicationConfig(
                    annotations = {
                        'key' : '0'
                        }, 
                    app_config_groups = [
                        openapi_client.models.v1alpha1/app_config_group.v1alpha1.AppConfigGroup(
                            component_ids = [
                                '0'
                                ], 
                            config_items = {
                                'key' : '0'
                                }, 
                            injection_type = '0', 
                            name = '0', )
                        ], 
                    apps = [
                        openapi_client.models.v1alpha1/component.v1alpha1.Component(
                            category = '0', 
                            cmd = '0', 
                            component_graphs = [
                                openapi_client.models.v1alpha1/component_graph.v1alpha1.ComponentGraph(
                                    component_id = '0', 
                                    graph_id = '0', 
                                    promql = '0', 
                                    sequence = 56, 
                                    title = '0', )
                                ], 
                            component_monitors = [
                                openapi_client.models.v1alpha1/component_monitor.v1alpha1.ComponentMonitor(
                                    interval = '0', 
                                    name = '0', 
                                    path = '0', 
                                    port = 56, 
                                    service_show_name = '0', )
                                ], 
                            cpu = 56, 
                            dep_service_map_list = [
                                openapi_client.models.v1alpha1/component_dep.v1alpha1.ComponentDep(
                                    dep_service_key = '0', )
                                ], 
                            deploy_version = '0', 
                            endpoints = openapi_client.models.v1alpha1/endpoints.v1alpha1.Endpoints(
                                endpoints_info = '0', 
                                endpoints_type = '0', 
                                service_cname = '0', ), 
                            extend_method = '0', 
                            extend_method_map = openapi_client.models.v1alpha1/component_extend_method_rule.v1alpha1.ComponentExtendMethodRule(
                                init_memory = 56, 
                                is_restart = 56, 
                                max_memory = 56, 
                                max_node = 56, 
                                min_memory = 56, 
                                min_node = 56, 
                                step_memory = 56, 
                                step_node = 56, ), 
                            image = '0', 
                            labels = {
                                'key' : '0'
                                }, 
                            language = '0', 
                            memory = 56, 
                            mnt_relation_list = [
                                openapi_client.models.v1alpha1/component_share_volume.v1alpha1.ComponentShareVolume(
                                    mnt_dir = '0', 
                                    mnt_name = '0', 
                                    service_share_uuid = '0', )
                                ], 
                            port_map_list = [
                                openapi_client.models.v1alpha1/component_port.v1alpha1.ComponentPort(
                                    container_port = 56, 
                                    is_inner_service = True, 
                                    is_outer_service = True, 
                                    port_alias = '0', 
                                    protocol = '0', 
                                    tenant_id = '0', )
                                ], 
                            probes = [
                                openapi_client.models.v1alpha1/component_probe.v1alpha1.ComponentProbe(
                                    id = 56, 
                                    cmd = '0', 
                                    failure_threshold = 56, 
                                    http_header = '0', 
                                    initial_delay_second = 56, 
                                    is_used = True, 
                                    mode = '0', 
                                    path = '0', 
                                    period_second = 56, 
                                    port = 56, 
                                    probe_id = '0', 
                                    scheme = '0', 
                                    service_id = '0', 
                                    success_threshold = 56, 
                                    timeout_second = 56, )
                                ], 
                            service_alias = '0', 
                            service_cname = '0', 
                            service_connect_info_map_list = [
                                openapi_client.models.v1alpha1/component_env.v1alpha1.ComponentEnv(
                                    attr_name = '0', 
                                    attr_value = '0', 
                                    container_port = 56, 
                                    is_change = True, 
                                    name = '0', )
                                ], 
                            service_env_map_list = [
                                openapi_client.models.v1alpha1/component_env.v1alpha1.ComponentEnv(
                                    attr_name = '0', 
                                    attr_value = '0', 
                                    container_port = 56, 
                                    is_change = True, 
                                    name = '0', )
                                ], 
                            service_id = '0', 
                            service_image = openapi_client.models.v1alpha1/image_info.v1alpha1.ImageInfo(
                                hub_password = '0', 
                                hub_url = '0', 
                                hub_user = '0', 
                                is_trust = True, 
                                namespace = '0', ), 
                            service_key = '0', 
                            service_name = '0', 
                            service_related_plugin_config = [
                                openapi_client.models.v1alpha1/component_plugin_config.v1alpha1.ComponentPluginConfig(
                                    attr = [
                                        openapi_client.models.v1alpha1/component_plugin_config/attr.v1alpha1.ComponentPluginConfig.attr()
                                        ], 
                                    build_version = '0', 
                                    cpu_required = 56, 
                                    create_time = '0', 
                                    memory_required = 56, 
                                    plugin_id = '0', 
                                    plugin_key = '0', 
                                    plugin_status = True, 
                                    service_id = '0', 
                                    service_meta_type = '0', )
                                ], 
                            service_share_uuid = '0', 
                            service_source = '0', 
                            service_type = '0', 
                            service_volume_map_list = [
                                openapi_client.models.v1alpha1/component_volume.v1alpha1.ComponentVolume(
                                    access_mode = '0', 
                                    file_content = '0', 
                                    mode = 56, 
                                    share_policy = '0', 
                                    volume_capacity = 56, 
                                    volume_name = '0', 
                                    volume_path = '0', 
                                    volume_type = '0', )
                                ], 
                            share_image = '0', 
                            share_type = '0', 
                            version = '0', )
                        ], 
                    group_key = '0', 
                    group_name = '0', 
                    group_version = '0', 
                    ingress_http_routes = [
                        openapi_client.models.v1alpha1/ingress_http_route.v1alpha1.IngressHTTPRoute(
                            component_key = '0', 
                            connection_timeout = 56, 
                            cookies = {
                                'key' : '0'
                                }, 
                            default_domain = True, 
                            headers = {
                                'key' : '0'
                                }, 
                            load_balancing = '0', 
                            location = '0', 
                            port = 56, 
                            proxy_buffer = True, 
                            proxy_buffer_numbers = 56, 
                            proxy_buffer_size = 56, 
                            proxy_header = {
                                'key' : '0'
                                }, 
                            request_body_size_limit = 56, 
                            request_timeout = 56, 
                            response_timeout = 56, 
                            ssl = True, 
                            websocket = True, )
                        ], 
                    ingress_stream_routes = [
                        openapi_client.models.v1alpha1/ingress_sream_route.v1alpha1.IngressSreamRoute(
                            component_key = '0', 
                            connection_timeout = 56, 
                            port = 56, 
                            protocol = '0', )
                        ], 
                    plugins = [
                        openapi_client.models.v1alpha1/plugin.v1alpha1.Plugin(
                            id = 56, 
                            build_source = '0', 
                            build_version = '0', 
                            category = '0', 
                            code_repo = '0', 
                            config_groups = [
                                openapi_client.models.v1alpha1/plugin_config_group.v1alpha1.PluginConfigGroup(
                                    id = 56, 
                                    build_version = '0', 
                                    config_name = '0', 
                                    injection = '0', 
                                    options = [
                                        openapi_client.models.v1alpha1/plugin_config_group_option.v1alpha1.PluginConfigGroupOption(
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
                            share_image = '0', )
                        ], 
                    template_version = '0', ),
                template_type = '0',
                version = '0',
                version_alias = '0',
        )

    def testV1CreateAppPaaSVersionRequest(self):
        """Test V1CreateAppPaaSVersionRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
