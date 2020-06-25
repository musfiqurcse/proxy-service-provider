from proxy_service_provider.apps.configuration.models.proxies import Proxies
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import NotFound


class ProxiesSerializer(ModelSerializer):

    class Meta:
        model = Proxies
        fields = (
            'id',
            'ip_address',
            'port_number',
            'proxy_provider_id',
            'last_successful_functionality_test',
            'is_tested',
            'last_found',
            'first_found'
        )



    def validate_ip_address(self,data):
        if self.instance is None:
            proxy= Proxies.objects.filter(ip_address=data)
            if len(proxy) > 0:
                raise serializers.ValidationError("This IP Address is already exist")
        else:
            proxy= Proxies.objects.filter(ip_address=data)
            if len(proxy) > 0 and self.instance.ip_address != data:
                raise serializers.ValidationError("This IP Address is already exist")
        return data

    def validate_port_number(self,data):
        if data is None or data == '' or len(data) <=1:
            raise serializers.ValidationError("Please provide a valid port number")
        return data

