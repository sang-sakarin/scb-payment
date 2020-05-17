"""
A libraly that provides a python interface to SCB Payment API
"""
import json
import uuid

from .business_code import BusinessCode
from .constants import ENDPOINTS
from .error import SCBPaymentError
from .request import basic_request


class Authorization():

    def __init__(self, api_key, api_secret, merchant, terminal, biller):
        self.api_key = api_key
        self.api_secret = api_secret
        self.merchant = merchant
        self.terminal = terminal
        self.biller = biller
        self.API_ROOT = ENDPOINTS["API_ROOT"]
        self.token = self._get_token()

    def _get_path(self, path_name, **kwargs):
        """
        Get full endpoint for a specific path.
        """
        return self.API_ROOT + ENDPOINTS[path_name].format(**kwargs)

    def _get_headers(self):
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['resourceOwnerId'] = str(uuid.uuid4())
        headers['requestUId'] = str(uuid.uuid4())
        headers['accept-language'] = 'EN'

        if getattr(self, "token", None) is not None:
            headers['authorization'] = "{0} {1}".format("Bearer", self.token)

        return headers

    def _get_token(self):
        url = self._get_path("OAUTH_TOKEN_PATH")

        payload = {}
        payload["applicationKey"] = self.api_key
        payload["applicationSecret"] = self.api_secret
        payload = json.dumps(payload)

        response = basic_request('POST', url, headers=self._get_headers(), payload=payload)

        if response['status']['code'] != BusinessCode.SUCCESS:
            raise SCBPaymentError("{0} {1}".format(response['status']['code'], response['status']['description']))

        return response['data']['accessToken']
