# coding: utf-8

"""
    bampli-api

    The API for the Business Amplifier project.  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: josemotta@bampli.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class FacilityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_facility(self, body, **kwargs):  # noqa: E501
        """Create a new Facility  # noqa: E501

        Adds a Facility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_facility(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Facility body: (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_facility_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_facility_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_facility_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new Facility  # noqa: E501

        Adds a Facility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_facility_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Facility body: (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_facility" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_facility`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/facility/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Facility',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_wip(self, body, **kwargs):  # noqa: E501
        """Create a new Wip  # noqa: E501

        Adds a Wip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_wip(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Wip body: (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_wip_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_wip_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_wip_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new Wip  # noqa: E501

        Adds a Wip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_wip_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Wip body: (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_wip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_wip`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wip/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Wip',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_facility(self, facilityid, **kwargs):  # noqa: E501
        """Delete a Facility  # noqa: E501

        Deletes a Facility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_facility(facilityid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facilityid: Identifier of the Facility (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_facility_with_http_info(facilityid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_facility_with_http_info(facilityid, **kwargs)  # noqa: E501
            return data

    def delete_facility_with_http_info(self, facilityid, **kwargs):  # noqa: E501
        """Delete a Facility  # noqa: E501

        Deletes a Facility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_facility_with_http_info(facilityid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facilityid: Identifier of the Facility (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['facilityid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_facility" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'facilityid' is set
        if ('facilityid' not in params or
                params['facilityid'] is None):
            raise ValueError("Missing the required parameter `facilityid` when calling `delete_facility`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'facilityid' in params:
            path_params['facilityid'] = params['facilityid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/facility/{facilityid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_wip(self, wipid, **kwargs):  # noqa: E501
        """Delete a Wip  # noqa: E501

        Deletes a Wip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_wip(wipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wipid: Identifier of the Wip (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_wip_with_http_info(wipid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_wip_with_http_info(wipid, **kwargs)  # noqa: E501
            return data

    def delete_wip_with_http_info(self, wipid, **kwargs):  # noqa: E501
        """Delete a Wip  # noqa: E501

        Deletes a Wip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_wip_with_http_info(wipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wipid: Identifier of the Wip (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wipid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_wip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wipid' is set
        if ('wipid' not in params or
                params['wipid'] is None):
            raise ValueError("Missing the required parameter `wipid` when calling `delete_wip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wipid' in params:
            path_params['wipid'] = params['wipid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wip/{wipid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_facility(self, facilityid, **kwargs):  # noqa: E501
        """Load an individual Facility  # noqa: E501

        Loads a Facility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility(facilityid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facilityid: Identifier of the Facility (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_facility_with_http_info(facilityid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_facility_with_http_info(facilityid, **kwargs)  # noqa: E501
            return data

    def get_facility_with_http_info(self, facilityid, **kwargs):  # noqa: E501
        """Load an individual Facility  # noqa: E501

        Loads a Facility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_facility_with_http_info(facilityid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str facilityid: Identifier of the Facility (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['facilityid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facility" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'facilityid' is set
        if ('facilityid' not in params or
                params['facilityid'] is None):
            raise ValueError("Missing the required parameter `facilityid` when calling `get_facility`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'facilityid' in params:
            path_params['facilityid'] = params['facilityid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/facility/{facilityid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Facility',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_wip(self, wipid, **kwargs):  # noqa: E501
        """Load an individual Wip  # noqa: E501

        Loads a Wip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wip(wipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wipid: Identifier of the Wip (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_wip_with_http_info(wipid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_wip_with_http_info(wipid, **kwargs)  # noqa: E501
            return data

    def get_wip_with_http_info(self, wipid, **kwargs):  # noqa: E501
        """Load an individual Wip  # noqa: E501

        Loads a Wip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wip_with_http_info(wipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wipid: Identifier of the Wip (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wipid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wipid' is set
        if ('wipid' not in params or
                params['wipid'] is None):
            raise ValueError("Missing the required parameter `wipid` when calling `get_wip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wipid' in params:
            path_params['wipid'] = params['wipid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wip/{wipid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Wip',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_facility(self, **kwargs):  # noqa: E501
        """Load the list of Facilities  # noqa: E501

        Loads list of Facilities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_facility(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int size: Size of the page to retrieve.
        :param float page: Number of the page to retrieve.
        :param str sort: Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC,city DESC
        :param str name: Allows to filter the collections of result by name
        :param str company_id: Allows to filter the collections of result by company_id
        :return: list[Facility]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_facility_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_facility_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_facility_with_http_info(self, **kwargs):  # noqa: E501
        """Load the list of Facilities  # noqa: E501

        Loads list of Facilities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_facility_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int size: Size of the page to retrieve.
        :param float page: Number of the page to retrieve.
        :param str sort: Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC,city DESC
        :param str name: Allows to filter the collections of result by name
        :param str company_id: Allows to filter the collections of result by company_id
        :return: list[Facility]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['size', 'page', 'sort', 'name', 'company_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_facility" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'size' in params:
            query_params.append(('$size', params['size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('$page', params['page']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('$sort', params['sort']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'company_id' in params:
            query_params.append(('company_id', params['company_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/facility/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Facility]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_wips(self, **kwargs):  # noqa: E501
        """Load the list of Wips  # noqa: E501

        Loads list of Wips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_wips(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int size: Size of the page to retrieve.
        :param float page: Number of the page to retrieve.
        :param str sort: Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC,city DESC
        :param str name: Allows to filter the collections of result by name
        :param str facility_id: Allows to filter the collections of result by facility_id
        :return: list[Wip]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_wips_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_wips_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_wips_with_http_info(self, **kwargs):  # noqa: E501
        """Load the list of Wips  # noqa: E501

        Loads list of Wips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_wips_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int size: Size of the page to retrieve.
        :param float page: Number of the page to retrieve.
        :param str sort: Order in which to retrieve the results. Multiple sort criteria can be passed. Example: sort=name ASC,city DESC
        :param str name: Allows to filter the collections of result by name
        :param str facility_id: Allows to filter the collections of result by facility_id
        :return: list[Wip]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['size', 'page', 'sort', 'name', 'facility_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_wips" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'size' in params:
            query_params.append(('$size', params['size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('$page', params['page']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('$sort', params['sort']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'facility_id' in params:
            query_params.append(('facility_id', params['facility_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wip/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Wip]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_facility(self, body, facilityid, **kwargs):  # noqa: E501
        """Update a Facility  # noqa: E501

        Stores a Facility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_facility(body, facilityid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Facility body: (required)
        :param str facilityid: Identifier of the Facility (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_facility_with_http_info(body, facilityid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_facility_with_http_info(body, facilityid, **kwargs)  # noqa: E501
            return data

    def update_facility_with_http_info(self, body, facilityid, **kwargs):  # noqa: E501
        """Update a Facility  # noqa: E501

        Stores a Facility  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_facility_with_http_info(body, facilityid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Facility body: (required)
        :param str facilityid: Identifier of the Facility (required)
        :return: Facility
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'facilityid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_facility" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_facility`")  # noqa: E501
        # verify the required parameter 'facilityid' is set
        if ('facilityid' not in params or
                params['facilityid'] is None):
            raise ValueError("Missing the required parameter `facilityid` when calling `update_facility`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'facilityid' in params:
            path_params['facilityid'] = params['facilityid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/facility/{facilityid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Facility',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_wip(self, body, wipid, **kwargs):  # noqa: E501
        """Update a Wip  # noqa: E501

        Stores a Wip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_wip(body, wipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Wip body: (required)
        :param str wipid: Identifier of the Wip (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_wip_with_http_info(body, wipid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_wip_with_http_info(body, wipid, **kwargs)  # noqa: E501
            return data

    def update_wip_with_http_info(self, body, wipid, **kwargs):  # noqa: E501
        """Update a Wip  # noqa: E501

        Stores a Wip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_wip_with_http_info(body, wipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Wip body: (required)
        :param str wipid: Identifier of the Wip (required)
        :return: Wip
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'wipid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_wip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_wip`")  # noqa: E501
        # verify the required parameter 'wipid' is set
        if ('wipid' not in params or
                params['wipid'] is None):
            raise ValueError("Missing the required parameter `wipid` when calling `update_wip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wipid' in params:
            path_params['wipid'] = params['wipid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wip/{wipid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Wip',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
