from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import NotFound
class ProxyProviderSerializer(ModelSerializer):
    proxy_provider_address = serializers.CharField(required=True, max_length=120, min_length=3)
    class Meta:
        model=ProxyProviders
        fields = (
            'proxy_provider_address',
            'is_https_filtered'
        )
        # last_updated_proxy_list = serializers.DateTimeField()
        read_only_fields = ('id','last_updated_proxy_list')

    # def create(self, validated_data):
    #     try:
    #         service_dict = {
    #             'proxy_provider_address': validated_data.get('proxy_provider_address')
    #         }
    #         save_proxy_provider = ProxyProviders.objects.create(**service_dict)
    #         save_proxy_provider.save()
    #         return save_proxy_provider
    #     except Exception as ex:
    #         raise NotFound('Error Occurred while creating new Service Provider')
    def validate_proxy_provider_address(self,data):
        if self.instance is None:
            proxy_provider= ProxyProviders.objects.filter(proxy_provider_address=data)
            if len(proxy_provider) > 0:
                raise serializers.ValidationError("This Proxy Address is already exist")
        else:
            proxy_provider = ProxyProviders.objects.filter(proxy_provider_address=data)
            if len(proxy_provider) > 0 and self.instance.proxy_provider_address != data:
                raise serializers.ValidationError("This Proxy Address is already exist")