import json

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from proxy_service_provider.apps.configuration.models.test_url import TestURL
from proxy_service_provider.apps.core.utils.response_utils import OutputMaker
from proxy_service_provider.apps.configuration.serializers.test_url_serializer import TestURLSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.serializers import serialize


class TestURLView(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = TestURL.objects.all()
    serializer_class = TestURLSerializer


    def create(self, request):
        try:
            # TODO: Implement the POST Request.
            output_maker = OutputMaker()
            data = request.data.get('data')
            output = {
                'status': False,
                'output': {}
            }
            test_url_serializer = TestURLSerializer(data=data)
            if test_url_serializer.is_valid():
                main_data = test_url_serializer.save()
                struct_data = json.loads(serialize('json', [main_data, ]))
                output_result = struct_data[0]['fields']
                response_data = output_maker.response_builder(message="",result="success",output=output_result)
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data = output_maker.response_builder(message=test_url_serializer.errors, result='error', output={})
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            return Response({
                'message': "Error occured while processing the request. Server Error",
                'status': 'error',
                'output': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'], url_name='Get TEST URL List', url_path='list')
    def get_proxy_list_provider(self, request, pk=None):
        try:
            test_urls = TestURL.objects.all()
            output_maker = OutputMaker()
            output = {
                'status': False,
                'output': {}
            }
            response_data = []
            for i in test_urls:
                data = {
                    'id': i.id,
                    'test_url_address': i.test_url_address,
                    'updated_time': i.updated_time.strftime('%d.%m.%Y %H:%M'),
                    'test_url_provider_name': i.test_url_provider_name,
                    'is_output_json': i.is_output_json
                }
                response_data.append(data)
            response_data = output_maker.response_builder(message="", result="success", output=response_data)
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as ex:
            print(ex)
            return Response({
                'message': "Error occured while processing the request. Server Error",
                'status': 'error',
                'output': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @action(detail=False, methods=['GET'], url_name='Get a Specific Functionality Test', url_path='func-test')
    def get_proxy_list_provider(self, request, pk=None):
        try:
            test_urls = TestURL.objects.all()
            output_maker = OutputMaker()
            output = {
                'status': False,
                'output': {}
            }
            response_data = []
            for i in test_urls:
                data = {
                    'id': i.id,
                    'test_url_address': i.test_url_address,
                    'updated_time': i.updated_time.strftime('%d.%m.%Y %H:%M'),
                    'test_url_provider_name': i.test_url_provider_name,
                    'is_output_json': i.is_output_json
                }
                response_data.append(data)
            response_data = output_maker.response_builder(message="", result="success", output=response_data)
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as ex:
            print(ex)
            return Response({
                'message': "Error occured while processing the request. Server Error",
                'status': 'error',
                'output': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)