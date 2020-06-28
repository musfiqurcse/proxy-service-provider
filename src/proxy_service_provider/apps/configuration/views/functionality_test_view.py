import json

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from proxy_service_provider.apps.configuration.models.proxy_functionality_test import ProxyFunctionalityTest
from proxy_service_provider.apps.core.utils.response_utils import OutputMaker
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.serializers import serialize


class ProxyFunctionalityTestView(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = ProxyFunctionalityTest.objects.all()



    def retrieve(self, request, pk=None):
        try:
            report = ProxyFunctionalityTest.objects.get(id=int(pk))
            output_maker = OutputMaker()
            output = {
                'status': False,
                'output': {}
            }
            if report != None:
                response_data = {
                        'id': report.id,
                        'test_url_address': report.test_url_id.test_url_address,
                        'created_time': report.created_time.strftime('%d.%m.%Y %H:%M'),
                        'ip_address': report.proxy_id.ip_address,
                        'port_number': report.proxy_id.port_number,
                        'is_test_passed': report.is_test_passed,
                        'test_mesasge': report.test_mesasge
                    }
                response_data = output_maker.response_builder(message="", result="success", output=response_data)
                return Response(response_data, status=status.HTTP_200_OK)
        except Exception as ex:
            print(ex)
            return Response({
                'message': "Error occured while processing the request. Server Error",
                'status': 'error',
                'output': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)