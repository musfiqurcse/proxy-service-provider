from django.db import models



class ProxyProvider(models.Model):
    # A timestamp for representing when this object was created
    created_time = models.DateTimeField(auto_now_add=True)

    # A timestamp for representing when this object was last updated
    updated_time = models.DateTimeField(auto_now=True)

