import requests
from typing import List, Dict
from RENXT_api.exceptions import RENXTApiException
from json import JSONDecodeError
from RENXT_api.models import Result
from ratelimit import limits


class RestAdapter:
    def __init__(self, hostname: str, api_key: str = '', oauth_key: str = ''):
        self.url = f"https://{hostname}"
        self._api_key = api_key
        self._oauth_key = oauth_key
    
    @limits(calls=10, period=1)
    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None):
        
        full_url = self.url + endpoint
        headers = {
            'Content-Type': 'application/json',
            'Bb-Api-Subscription-Key': self._api_key,
            'Authorization': self._oauth_key
        }
        try:
            response = requests.request(method=http_method, url=full_url, headers=headers, params=ep_params, json=data)
        except requests.exceptions.RequestException as e:
            raise RENXTApiException('Request failed') from e
        data_out = None
        if (http_method != 'PATCH') and (http_method != 'DELETE'):
            try:
                data_out = response.json()
            except (ValueError, JSONDecodeError) as e:
                raise RENXTApiException('Bad JSON in response') from e
        if 299 >= response.status_code >= 200:
            return Result(response.status_code, message=response.reason, data=data_out)
        raise RENXTApiException(f'{response.status_code}: {response.reason}')

    def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)
    
    def post(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)
    
    def delete(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='DELETE', endpoint=endpoint, ep_params=ep_params, data=data)
    
    def patch(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='PATCH', endpoint=endpoint, ep_params=ep_params, data=data)
