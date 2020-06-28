from proxy_service_provider.apps.configuration.serializers.proxy_serializer import ProxiesSerializer
from proxy_service_provider.apps.configuration.models.proxies import  Proxies
from proxy_service_provider.apps.configuration.models.test_url import  TestURL
from proxy_service_provider.apps.configuration.models.proxy_functionality_test import  ProxyFunctionalityTest
from proxy_service_provider.apps.configuration.services.proxy_fetcher import  ProxyFetching
from django.db.models import Q
from datetime import datetime
import time

class ProxyServices:

    def bulk_create(self, proxy_provider, ip_list: list):
        counter = 0
        for item in ip_list:
            data = {
                'ip_address': item[0],
                'port_number': item[1],
                'proxy_provider_id': proxy_provider.id,
                'is_tested': False,
                'last_found': datetime.now(),
                'first_found': datetime.now()
            }
            i = self.create(data)
            if i is not None:
                counter += 1
        return counter

    def bulk_delete(self, proxy_provider_id, ip_list: list):
        counter = 0
        try:
            find_proxy = Proxies.objects.filter(proxy_provider_id=proxy_provider_id).exclude(ip_address__in=ip_list)
            counter = find_proxy.count()
            find_proxy.delete()
            return counter
        except Exception as ex:
            return counter, []

    def bulk_update(self, proxy_provider_id, ip_list: list):
        counter = 0
        only_ips = [i[0] for i in ip_list]
        # Delete not listed ip_address
        counts = self.bulk_delete(proxy_provider_id=proxy_provider_id,ip_list=only_ips)
        find_existed_ip = Proxies.objects.values_list('ip_address').filter(proxy_provider_id=proxy_provider_id)
        find_existed_ip.update(last_found = datetime.now())
        list_find_existed_ip = list(find_existed_ip)
        existed_proxies = len(list_find_existed_ip)
        for item in ip_list:
            if item[0] not in list_find_existed_ip:
                data = {
                    'ip_address': item[0],
                    'port_number': item[1],
                    'proxy_provider_id': proxy_provider_id,
                    'is_tested': False,
                    'last_found': datetime.now(),
                    'first_found': datetime.now()
                }
                i = self.create(data)
                if i is not None:
                    counter += 1
        return counter+existed_proxies


    def perform_functionality_test(self, provider_id: id, test_url_id: id):
        try:
            proxies = Proxies.objects.filter(proxy_provider_id=provider_id)
            test_url_id = TestURL.objects.get(id=test_url_id)
            proxy_fetching = ProxyFetching()
            count = 0
            for i in proxies:
                print(i)
                count +=1
                output = proxy_fetching.pass_proxy_test(proxy_address=i.ip_address,proxy_port=i.port_number,test_url=test_url_id.test_url_address)
                i.is_tested = output['result']
                i.last_successful_functionality_test = datetime.now()
                i.save()
                result_data = {
                    'proxy_id': i,
                    'test_url_id':test_url_id,
                    'is_test_passed': output['result'],
                    'test_mesasge': output['output']
                }
                print(result_data)
                func_test = ProxyFunctionalityTest(**result_data)
                func_test.save()
            return None
        except Exception as ex:
            print(ex)
            return None

    def create(self, kw: dict):
        """
        :type kw: object
        """
        proxy = ProxiesSerializer(data=kw)
        if proxy.is_valid():
            proxy.save()
            return proxy
        else:
            return None
