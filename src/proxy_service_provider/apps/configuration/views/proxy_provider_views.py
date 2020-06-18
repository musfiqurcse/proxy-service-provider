from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders
from proxy_service_provider.apps.core.utils.response_utils import OutputMaker
from proxy_service_provider.apps.configuration.services.ProxyProviderServices import ProxyProviderService,ProxyProviderSerializer
from rest_framework.response import Response

class ProxyProviderView(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = ProxyProviders.objects.all()
    serializer_class = ProxyProviderSerializer


    def create(self, request):
        try:
            # TODO: Implement the POST Request.
            output_maker = OutputMaker()
            proxy_service_provider = ProxyProviderService()
            output = proxy_service_provider.create_proxy(request.data.get('data'))
            if output['status'] == True:
                response_data = output_maker.response_builder(message="",result="success",output=output['output'])
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data = output_maker.response_builder(message=output['output'], result='error', output={})
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            return Response({
                'message': "Error occured while processing the request. Server Error",
                'status': 'error',
                'output': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
