from django.db import models
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import JSONField


class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_time = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        ordering = ['-created_time', '-updated_time']