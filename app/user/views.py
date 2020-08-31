from rest_framework import generics, authentication, permissions
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


class ManageUserView(generics.RetrieveUpdateAPIView):
    """ Leírás: Manage the authenticated user """
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        """ Leírás: Retrieve and return authentication user """
        return self.request.user
