
from proxy_service_provider.apps.configuration.serializers.proxy_serializer import ProxiesSerializer
from datetime import datetime
class ProxyServices:

    def bulk_create(self, proxy_provider, ip_list: list):
        counter  = 0
        for item in ip_list:
            data = {}
            data['ip_address']=item[0]
            data['port_number']=item[1]
            data['proxy_provider_id'] = proxy_provider
            data['is_tested'] = False
            data['last_found'] = datetime.now()
            data['first_found'] = datetime.now()
            i = self.create(data)
            if i != None:
                counter +=1
        return counter


    def create(self, kw: dict):
        proxy = ProxiesSerializer(data=kw)
        if proxy.is_valid():
            proxy.save()
            return proxy
        else:
            return None

