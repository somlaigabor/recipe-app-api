from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import UserSerializer, AuthTokenSerialSerializer
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    """ Leírás: Create a new user in the system """
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """ Leírás: Create a new auth token for user """
    serializer_class = AuthTokenSerialSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
