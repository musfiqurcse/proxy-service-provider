from proxy_service_provider.apps.configuration.serializers.proxy_service_provider_serializer import \
    ProxyProviderSerializer
from django.core.serializers import serialize
import json
from rest_framework.exceptions import NotFound
from proxy_service_provider.apps.configuration.services.proxy_fetcher import ProxyFetching
from proxy_service_provider.apps.configuration.services.proxy_services import ProxyServices
from  proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders
from datetime import datetime
from datetime import timedelta


class ProxyProviderService:

    def get_a_proxy_list_provider(self, id: int):
        try:
            return ProxyProviders.objects.get(pk=id)
        except Exception as ex:
            return NotFound("The proxy provider information not found.")

    # Service for create new Proxy
    def create_proxy_list_providers_with_proxies(self, data: dict):
        try:
            serialized_data = ProxyProviderSerializer(data=data)
            if serialized_data.is_valid():
                main_data = serialized_data.save()
                main_data.last_updated_proxy_list = datetime.now()
                proxy_fetcher = ProxyFetching()
                proxy_list = proxy_fetcher.fetch_data_from_proxy(url=data['proxy_provider_address'],
                                                                        https_check=data['is_https_filtered'])
                proxy_service = ProxyServices()
                total_proxies = proxy_service.bulk_create(main_data,proxy_list)
                main_data.new_proxies= total_proxies
                struct_data = json.loads(serialize('json', [main_data, ]))
                output_result = struct_data[0]['fields']
                main_data.save()
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
            print('Error occurred while creating proxy provider')
            print(ex)
            return NotFound(ex)

    def update_proxy_list_provider_with_proxies(self, proxy_provider_id, data: dict):
        try:
            initial_proxy_list_provider = self.get_a_proxy_list_provider(id = proxy_provider_id)
            last_updated_time = initial_proxy_list_provider.updated_time + timedelta(minutes=initial_proxy_list_provider.time_interval)
            if last_updated_time < datetime.now():
                proxy_list_provider = ProxyProviderSerializer(initial_proxy_list_provider, data=data)
                if proxy_list_provider.is_valid():
                    updated_proxy_list_provider = proxy_list_provider.save()
                    proxy_fetcher = ProxyFetching()
                    proxy_list = proxy_fetcher.fetch_data_from_proxy(url=data['proxy_provider_address'],
                                                                     https_check=data['is_https_filtered'])
                    proxy_services = ProxyServices()
                    total_new_proxies = proxy_services.bulk_update(proxy_provider_id=initial_proxy_list_provider.id,ip_list=proxy_list)
                    initial_proxy_list_provider.new_proxies = total_new_proxies
                    initial_proxy_list_provider.save()
                    struct_data = json.loads(serialize('json', [initial_proxy_list_provider, ]))
                    output_result = struct_data[0]['fields']
                    return {
                        'status': True,
                        'output': output_result
                    }
                return {
                    'status': False,
                    'output': proxy_list_provider.errors
                }
            else:
                return {
                    'status': False,
                    'output': "This proxy list provider can update after {0}".format(last_updated_time.strftime('%d.%m.%Y %H:%M'))
                }

        except Exception as ex:
            return NotFound(ex)

    def get_specific_proxy_provider_information(self, id: int):
        try:
            proxy_provider = self.get_a_proxy_list_provider(id)
            if proxy_provider:
                return {
                    'status': True,
                    'output': {
                        'id': proxy_provider.id,
                        'proxy_provider_address': proxy_provider.proxy_provider_address,
                        'updated_time': proxy_provider.updated_time.strftime('%d.%m.%Y %H:%M'),
                        'is_https_filtered': proxy_provider.is_https_filtered,
                        'time_interval': proxy_provider.time_interval,
                        'old_proxies': proxy_provider.old_proxies,
                        'new_proxies': proxy_provider.new_proxies,
                    }
                }
            return {
                'status': True,
                'output': "No Proxy Provider information Found."
            }

        except Exception as ex:
            print(ex)
            return NotFound(ex)


    def get_list_of_proxy_provider(self):
        try:
            get_all_provider_list = ProxyProviders.objects.all()
            response_data = []
            for i in get_all_provider_list:
                data = {
                    'id': i.id,
                    'proxy_provider_address': i.proxy_provider_address,
                    'updated_time': i.updated_time.strftime('%d.%m.%Y %H:%M'),
                    'is_https_filtered': i.is_https_filtered
                }
                response_data.append(data)
            return {
                'status': True,
                'output': response_data
            }
        except Exception as ex:
            print(ex)
            return NotFound(ex)

    def view_proxy(self, ):
        try:
            pass
        except Exception as ex:
            print(ex)
