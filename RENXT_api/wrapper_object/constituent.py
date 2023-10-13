from RENXT_api.rest_adapter import RestAdapter 
from RENXT_api.models import *


class Constituent():
    def __init__(self, rest_adapter: RestAdapter):
        self._rest_adapter = rest_adapter
    
    def search(self, search_text: str, include_inactive: bool = False,
                           search_field: str = '', strict_search: bool = False,
                           limit: int = 0, offset: int = 0) -> Result:
        params = {
            'search_text': search_text,
            'include_inactive': include_inactive,
            'search_field': search_field,
            'strict_search': strict_search,
            'limit': limit,
            'offset': offset
        }
        result = self._rest_adapter.get(endpoint='/constituent/v1/constituents/search', ep_params=params)
        bruh = result.data['value']
        constituents = []
        if bruh:
            for e in bruh:
                constituents.append(ConstituentSearch(**e))
        result.data = constituents
        return result
    
    def single_address_list(self, constituent_id: str, include_inactive: bool = False):
        params = {
            #'constituent_id': constituent_id,
            'include_inactive': include_inactive
        }
        result = self._rest_adapter.get(endpoint=f'/constituent/v1/constituents/{constituent_id}/addresses', ep_params=params)
        okay = result.data['value']
        addresses = []
        if result:
            for e in okay:
                addresses.append(AddressList(**e))
        result.data = addresses
        return result
        
    def edit_address():
        pass
        
    def single_email_address_list(self, constituent_id: str, include_inactive: bool = False):
        params = {
            'constituent_id': constituent_id,
            'include_inactive': include_inactive
        }
        result = self._rest_adapter.get(endpoint='/constituent/v1/constituents/215856/emailaddresses', ep_params=params)
        okay = result.data['value']
        emails = []
        if result:
            for e in okay:
                emails.append(Email(**e))
        result.data = emails
        return result

    def single_phone_list():
        pass

    def edit_phone():
        pass

    def edit():
        pass
