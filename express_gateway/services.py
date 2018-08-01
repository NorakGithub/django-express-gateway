import logging

import requests
from django.conf import settings
from rest_framework.exceptions import ValidationError

log = logging.getLogger('django')


def get_headers() -> dict:
    return {'Authorization': f'apiKey {settings.CAS_API_KEY}'}


def handle_error(url, data, response):
    if response.status_code not in range(200, 299):
        log.error(url)
        log.error(get_headers())
        log.error(data)
        raise ValidationError(response.json())


def create_user(**kwargs):
    """
    Expected kwargs are firstName, lastName, email, password
    """
    assert kwargs.get('firstName')
    assert kwargs.get('lastName')
    assert kwargs.get('email')
    assert kwargs.get('password')

    kwargs['faIdPrefix'] = 'FA01'
    url = settings.CAS_URL + '/auth/user/'
    response = requests.post(url=url, headers=get_headers(), json=kwargs)
    log.info(f'creating {kwargs}')
    handle_error(url, kwargs, response)

    return response.json()


def authenticate_user(username: str, password: str):
    url = settings.CAS_URL + '/auth/token/'
    data = {'username': username, 'password': password}
    response = requests.post(url=url, json=data)
    log.info(f'authentication {data}')
    handle_error(url, data, response)

    return response.json()
