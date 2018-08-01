===========================
Express Gateway With Django
===========================
Integrating Django with Express Gateway

------------
Requirements
------------
- Python 3 or later
- Django 2 or later
- Django Rest Framework 3.7 or later
- Requests 2.19 or later

------------
Installation
------------

Install with pip

.. code-block:: bash

    $ pip install django_express_gateway

---------------
Getting Started
---------------
Add `express_gateway` to your `INSTALLED_APPS`

.. code-block:: python
    
    INSTALLED_APPS = [
        ...
        'express_gateway',
    ]
    
Add authentication to DRF default authentication settings

.. code-block:: python

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'express_gateway.authentications.AuthUserAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
        ...
    }

Finally add Centralize Authentication URL and API Key

.. code-block:: python

    # Config data should get from environment variable
    CAS_URL = 'https://mycas-server.com'
    CAS_API_KEY = 'testingApiKey'
