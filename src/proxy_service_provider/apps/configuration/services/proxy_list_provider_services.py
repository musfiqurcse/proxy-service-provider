from proxy_service_provider.apps.configuration.serializers.proxy_service_provider_serializer import ProxyProviderSerializer
from django.core.serializers import serialize
import json
from rest_framework.exceptions import NotFound
from proxy_service_provider.apps.configuration.services.proxy_fetcher import ProxyFetching


class ProxyProviderService:

    # Service for create new Proxy
    def create_proxy(self, data: dict):
        try:
            serialized_data = ProxyProviderSerializer(data=data)
            if serialized_data.is_valid():
                main_data = serialized_data.save()
                struct_data = json.loads(serialize('json', [main_data , ]))
                output_result = struct_data[0]['fields']
                chk = ProxyFetching()
                jk = chk.fetch_data_from_proxy(url=data['proxy_provider_address'],https_check=data['https'])
                output_result['']
                response = {
                    'status': True,
                    'output': output_result
                }
            else:
                response = {
                    'status': False,
                    'output': serialized_data.errors
                }
            return response
        except Exception as ex:
            return NotFound(ex)

    def view_proxy(self,):
        try:
            pass
        except Exception as ex:
            print(ex)
