"""
A libraly that provides a python interface to SCB Payment API
"""

import requests


def basic_request(method, url, headers={}, payload={}):
    return requests.request(method, url, headers=headers, data=payload).json()
