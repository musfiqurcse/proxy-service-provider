from django.db import models
from proxy_service_provider.apps.core.models import TimestampedModel
from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders

class Proxies(TimestampedModel):

    proxy_provider_id = models.ForeignKey(ProxyProviders, related_name='proxy_providers_id', on_delete=models.CASCADE)
    ip_address = models.CharField(name="IP Address", max_length=60, blank=True,null=True)
    port_number = models.CharField(name="Port Number", max_length=60, blank=True,null=True)
    last_successful_functionality_test = models.DateTimeField(name='Last Functionality Test', )
    last_found = models.DateTimeField(name='Last Found Proxies',)
    first_found = models.DateTimeField(name='First Found Proxies',)
    latest_functional_test_url = models.CharField(name='Functional Test URL', blank=True, null=True, max_length=120)


