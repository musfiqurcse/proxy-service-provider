from django.conf.urls import url
from django.urls import include,path
from rest_framework import routers
from proxy_service_provider.apps.configuration.views.proxy_provider_views import ProxyProviderView
from proxy_service_provider.apps.configuration.views.test_url_view import TestURLView
from proxy_service_provider.apps.configuration.views.functionality_test_view import ProxyFunctionalityTestView



router =  routers.SimpleRouter()
router.register('proxy-service-provider', ProxyProviderView, basename='proxy-service-provider')
router.register('test-url', TestURLView, basename='Test URL')
router.register('functional-test', ProxyFunctionalityTestView, basename='Functional Test')



urlpatterns = [
    url(r'^', include(router.urls)),
]
