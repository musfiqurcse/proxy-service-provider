from django.conf.urls import url
from django.urls import include,path
from rest_framework import routers
from proxy_service_provider.apps.configuration.views.proxy_provider_views import ProxyProviderView



router =  routers.SimpleRouter()
router.register('proxy-service-provider', ProxyProviderView, basename='proxy-service-provider')



urlpatterns = [
    url(r'^', include(router.urls)),
]
