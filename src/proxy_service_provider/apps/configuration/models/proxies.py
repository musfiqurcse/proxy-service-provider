from django.db import models
from proxy_service_provider.apps.core.models import TimestampedModel
from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders

class Proxies(TimestampedModel):

    proxy_provider_id = models.ForeignKey(ProxyProviders, related_name='proxy_providers_proxy_ids', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=60, blank=True,null=True, unique=True)
    port_number = models.CharField(max_length=60, blank=True,null=True)
    last_successful_functionality_test = models.DateTimeField(blank=True,null=True)
    last_found = models.DateTimeField( blank=True,null=True)
    first_found = models.DateTimeField( blank=True,null=True)
    is_tested = models.BooleanField('Is Proxy Tester', default=False)




