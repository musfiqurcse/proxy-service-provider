"""
ASGI config for proxy_service_provider project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
# Todo find the ASGI configuration for production.
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proxy_service_provider.settings')

application = get_asgi_application()
