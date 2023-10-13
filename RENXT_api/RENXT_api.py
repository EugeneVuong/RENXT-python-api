from RENXT_api.rest_adapter import RestAdapter
from RENXT_api.models import *
from RENXT_api.wrapper_object.constituent import Constituent

class RENXTApi:
    def __init__(self, hostname: str = 'api.sky.blackbaud.com', api_key: str = '', oauth_key: str = ''):
        self._rest_adapter = RestAdapter(hostname=hostname, api_key=api_key, oauth_key=oauth_key)
        
        # Wrapper Object
        self.constituent = Constituent(self._rest_adapter)


    
        
    
    

    def edit_email_address_temp(self, email_address_id: str) -> Result:
        params = {
            "type": "Business - Email"
        }
        result = self._rest_adapter.patch(endpoint=f'/constituent/v1/emailaddresses/{email_address_id}', data=params)

        return result
    
    def delete_email_address(self, email_address_id: str) -> Result:
        return self._rest_adapter.delete(endpoint=f'/constituent/v1/emailaddresses/{email_address_id}')

