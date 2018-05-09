from django.shortcuts import render
from .serializers import DeviceSerializer
from .models import DeviceModel
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken
from .serializers import JWTSerializer



# Create your views here.

class DeviceView(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (IsAuthenticated,)

class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer