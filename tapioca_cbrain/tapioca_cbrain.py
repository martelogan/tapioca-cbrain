# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from resource_mapping import RESOURCE_MAPPING


class CbrainClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://portal.cbrain.mcgill.ca/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        kwargs = super(CbrainClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        kwargs['headers'] = {'Accept': 'application/json'}

        kwargs['params'] = {'cbrain_api_token': api_params.get('cbrain_api_token')}

        return kwargs

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Cbrain = generate_wrapper_from_adapter(CbrainClientAdapter)
