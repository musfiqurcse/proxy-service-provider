from django.contrib import admin
from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders
from proxy_service_provider.apps.configuration.models.test_url import TestURL
# Register your models here.
admin.site.register(ProxyProviders)
admin.site.register(TestURL)
