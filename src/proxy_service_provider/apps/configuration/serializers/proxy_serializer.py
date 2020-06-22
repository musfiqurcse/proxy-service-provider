from proxy_service_provider.apps.configuration.models.proxies import Proxies
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import NotFound


class ProxiesSerializer(ModelSerializer):

    class Meta:
        model = Proxies
        fields = (
            'ip_address',
            'port_number',
            'proxy_provider_id',
            'last_successful_functionality_test',
            'is_tested',
            'last_found',
            'first_found'
        )

