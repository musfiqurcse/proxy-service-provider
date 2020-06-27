from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from proxy_service_provider.apps.configuration.models.proxy_providers import ProxyProviders
from proxy_service_provider.apps.core.utils.response_utils import OutputMaker
from proxy_service_provider.apps.configuration.services.proxy_list_provider_services import ProxyProviderService,ProxyProviderSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from proxy_service_provider.apps.configuration.services.proxy_fetcher import ProxyFetching



class ProxyProviderView(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = ProxyProviders.objects.all()
    serializer_class = ProxyProviderSerializer


    def create(self, request):
        try:
            # TODO: Implement the POST Request.
            output_maker = OutputMaker()
            data = request.data.get('data')
            proxy_service_provider = ProxyProviderService()
            output = {
                'status': False,
                'output': {}
            }
            output = proxy_service_provider.create_proxy_list_providers_with_proxies(request.data.get('data'))
            # Buffer Code
            # chk = ProxyFetching()
            # res = chk.fetch_data_from_proxy(url=data['proxy_provider_address'],https_check=data['https'])
            # Buffer Code End
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


    @action(detail=True, methods=['PUT'], url_name='Update Proxy List Provider', url_path='update-proxy')
    def update_proxy(self, request, pk=None):
        try:
            # TODO: Implement the POST Request.
            output_maker = OutputMaker()
            data = request.data.get('data')
            proxy_service_provider = ProxyProviderService()
            output = {
                'status': False,
                'output': {}
            }
            output = proxy_service_provider.update_proxy_list_provider_with_proxies(proxy_provider_id=pk,data=request.data.get('data'))
            if output['status'] == True:
                response_data = output_maker.response_builder(message="",result="success",output=output['output'])
                return Response(response_data, status=status.HTTP_200_OK)
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

    # @action(detail=False, methods=['GET'], url_name='GET Specific Proxy Provider', url_path='details')
    def retrieve(self, request, pk):
        try:
            proxy_service_provider = ProxyProviderService()
            output_maker = OutputMaker()
            output = {
                'status': False,
                'output': {}
            }
            output = proxy_service_provider.get_specific_proxy_provider_information(id=pk)
            if output['status'] == True:
                response_data = output_maker.response_builder(message="", result="success", output=output['output'])
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = output_maker.response_builder(message=output['output'], result='error', output={})
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            print(ex)
            return Response({
                'message': "Error occured while processing the request. Server Error",
                'status': 'error',
                'output': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @action(detail=False, methods=['GET'], url_name='Get Proxy List Provider', url_path='list')
    def get_proxy_list_provider(self, request, pk=None):
        try:
            proxy_service_provider = ProxyProviderService()
            output_maker = OutputMaker()
            output = {
                'status': False,
                'output': {}
            }
            output = proxy_service_provider.get_list_of_proxy_provider()
            if output['status'] == True:
                response_data = output_maker.response_builder(message="",result="success",output=output['output'])
                return Response(response_data, status=status.HTTP_200_OK)
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
