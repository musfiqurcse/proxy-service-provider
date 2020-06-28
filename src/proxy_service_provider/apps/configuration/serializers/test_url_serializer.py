from proxy_service_provider.apps.configuration.models.test_url import TestURL
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import NotFound


class TestURLSerializer(ModelSerializer):

    class Meta:
        model = TestURL
        fields = (
            'id',
            'test_url_address',
            'test_url_provider_name',
            'is_output_json',
            'updated_time',
        )
