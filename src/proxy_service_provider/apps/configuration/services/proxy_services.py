from proxy_service_provider.apps.configuration.serializers.proxy_serializer import ProxiesSerializer
from datetime import datetime


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
