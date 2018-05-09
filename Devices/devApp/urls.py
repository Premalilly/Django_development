from django.conf.urls import url, include
from rest_framework import routers
from .views import DeviceView
from .views import ObtainJWTView
router = routers.DefaultRouter()
router.register(r'devices', DeviceView)

urlpatterns = [
    #url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^root/',include(router.urls)),
    url(r'login/', view=ObtainJWTView.as_view(), name='login'),
]

