from django.db import models
from proxy_service_provider.apps.core.models import TimestampedModel
from proxy_service_provider.apps.configuration.models.proxies import Proxies
from proxy_service_provider.apps.configuration.models.test_url import TestURL

class ProxyFunctionalityTest(TimestampedModel):

    proxy_id = models.ForeignKey(Proxies, related_name='proxy_test_url_ids', on_delete=models.CASCADE)
    test_mesasge = models.TextField('Test Report Message', max_length=500, blank=True, null=True )
    is_test_passed = models.BooleanField('Is Proxy Test Passed',default=False)
    test_url_id = models.ForeignKey(TestURL, related_name='test_url_func_test_ids', on_delete=models.CASCADE)
