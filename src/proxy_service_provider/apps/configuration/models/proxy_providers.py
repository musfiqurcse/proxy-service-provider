from django.db import models



class ProxyProviders(models.Model):

    # Proxy List Address
    proxy_provider_address = models.CharField(name='Proxy Provider Address', max_length=120, unique=True)

    # Last Updated Proxy List time
    last_updated_proxy_list = models.DateTimeField(name='Last Updated Proxy List', blank=True, null=True)

    # A timestamp for representing when this object was created
    created_time = models.DateTimeField(auto_now_add=True)

    # A timestamp for representing when this object was last updated
    updated_time = models.DateTimeField(auto_now=True)

    # todo: add proxy list time interval for update the list

