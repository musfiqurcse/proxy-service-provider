from django.db import models



class ProxyProviders(models.Model):

    # Proxy List Address
    proxy_provider_address = models.CharField(max_length=120, blank=False, unique=True, null=False)
    # Auto Detect HTTPS
    is_https_filtered = models.BooleanField('Is HTTPS Filtered in the list', default=True)
    # Last Updated Proxy List time
    # last_updated_proxy_list = models.DateTimeField(blank=True, null=True,auto_now=True)

    # A timestamp for representing when this object was created
    created_time = models.DateTimeField(auto_now_add=True)

    # A timestamp for representing when this object was last updated
    updated_time = models.DateTimeField(auto_now=True)

    #Update Time Interval
    time_interval = models.IntegerField('Time Interval for Update the Proxy', default=10)
    old_proxies = models.IntegerField(default=0)
    new_proxies = models.IntegerField(default=0)

    # TODO: add proxy list time interval for update the list



