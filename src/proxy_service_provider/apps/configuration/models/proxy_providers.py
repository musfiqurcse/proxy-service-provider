from django.db import models



class ProxyProviders(models.Model):

    proxy_provider_address = models.CharField(name='Proxy Provider Address', max_length=120, unique=True)
    # A timestamp for representing when this object was created
    created_time = models.DateTimeField(auto_now_add=True)

    # A timestamp for representing when this object was last updated
    updated_time = models.DateTimeField(auto_now=True)

