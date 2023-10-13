from RENXT_api.rest_adapter import RestAdapter
from RENXT_api.models import *

class RENXTApi:
    def __init__(self, hostname: str = 'api.sky.blackbaud.com', api_key: str = '', oauth_key: str = ''):
        self._rest_adapter = RestAdapter(hostname=hostname, api_key=api_key, oauth_key=oauth_key)


    # Constituent
    def search_constituent(self, search_text: str, include_inactive: bool = False,
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
                constituents.append(Constituent_Search(**e))
        result.data = constituents
        return result
    
    def get_single_constituent_email_list(self, constituent_id: str, include_inactive: bool = False) -> List[Email]:
        params = {
            'constituent_id': constituent_id,
            'include_inactive': include_inactive
        }
        result = self._rest_adapter.get(endpoint='/constituent/v1/constituents/215856/emailaddresses', ep_params=params).data['value']
        emails = []
        if result:
            for e in result:
                emails.append(Email(**e))
        return emails

    def edit_email_address_temp(self, email_address_id: str) -> Result:
        params = {
            "type": "Business - Email"
        }
        result = self._rest_adapter.patch(endpoint=f'/constituent/v1/emailaddresses/{email_address_id}', data=params)

        return result
    
    def delete_email_address(self, email_address_id: str) -> Result:
        return self._rest_adapter.delete(endpoint=f'/constituent/v1/emailaddresses/{email_address_id}')

