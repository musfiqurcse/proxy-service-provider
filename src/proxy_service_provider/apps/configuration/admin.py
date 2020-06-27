from django.contrib import admin
from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders
# Register your models here.
admin.site.register(ProxyProviders)
