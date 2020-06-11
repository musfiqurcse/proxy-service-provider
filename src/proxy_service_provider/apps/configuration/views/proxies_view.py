from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders
from proxy_service_provider.apps.core.utils.response_utils import OutputMaker
class ProxyProviderView(APIView):
    permission_classes = (AllowAny, )
    # queryset = ProxyProviders.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            output_maker = OutputMaker()
            pass
        except Exception as ex:
            print(ex)
