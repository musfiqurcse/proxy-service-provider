from django.db import models
from proxy_service_provider.apps.core.models import TimestampedModel



class TestURL(TimestampedModel):

    test_url_address = models.CharField('Test URL Address', max_length=255, blank=False,null=False)
    test_url_provider_name = models.CharField('Test URL Provider Name', max_length=255, blank=False, null=False)
    is_output_json = models.BooleanField('Is Output JSON', default=True)


