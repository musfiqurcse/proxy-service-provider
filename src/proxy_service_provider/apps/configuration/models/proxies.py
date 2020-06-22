from django.db import models
from proxy_service_provider.apps.core.models import TimestampedModel
from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders

class Proxies(TimestampedModel):

    proxy_provider_id = models.ForeignKey(ProxyProviders, related_name='proxy_providers_proxy_ids', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=60, blank=True,null=True)
    port_number = models.CharField(max_length=60, blank=True,null=True)
    last_successful_functionality_test = models.DateTimeField()
    last_found = models.DateTimeField(auto_now=True)
    first_found = models.DateTimeField(auto_now_add=True)
    latest_functional_test_url = models.CharField(blank=True, null=True, max_length=120)



