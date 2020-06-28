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


    def validate_test_url_address(self,data):
        if self.instance is None:
            test_url_address= TestURL.objects.filter(test_url_address=data)
            if len(test_url_address) > 0:
                raise serializers.ValidationError("This TEST URL Address is already exist")
        else:
            test_url_address = TestURL.objects.filter(test_url_address=data)
            if len(test_url_address) > 0 and self.instance.test_url_address != data:
                raise serializers.ValidationError("This TEST URL Address is already exist")
        return data