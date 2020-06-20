from django.db import models
from proxy_service_provider.apps.core.models import TimestampedModel
from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders
from proxy_service_provider.apps.configuration.models.proxies import Proxies
class ProxyFunctionalityTest(models.Model):

    test_mesasge = models.TextField('Test Report Message', max_length=500, blank=True, null=True )
    is_test_passed = models.BooleanField('Is Proxy Test Passed',default=False)
    test_conduct_date = models.DateTimeField(auto_now=True)
    proxy_id = models.ForeignKey(ProxyProviders, related_name='proxy_providers_id', on_delete=models.CASCADE)