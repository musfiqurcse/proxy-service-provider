from django.db import models



class ProxyProviders(models.Model):

    # Proxy List Address
    proxy_provider_address = models.CharField(max_length=120, blank=False, unique=True, null=False)

    # Last Updated Proxy List time
    last_updated_proxy_list = models.DateTimeField(blank=True, null=True,auto_now=True)

    # A timestamp for representing when this object was created
    created_time = models.DateTimeField(auto_now_add=True)

    # A timestamp for representing when this object was last updated
    updated_time = models.DateTimeField(auto_now=True)

    # TODO: add proxy list time interval for update the list

