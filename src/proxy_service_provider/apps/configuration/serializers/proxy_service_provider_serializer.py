from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders
from rest_framework.serializers import Serializer, ModelSerializer

class ProxyProviderSerializer(ModelSerializer):

    class Meta:
        model=ProxyProviders
        fields = (
            'id',
            'proxy_provider_address',
            'last_updated_proxy_list',
            'updated_time'
        )
