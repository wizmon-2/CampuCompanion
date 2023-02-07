from rest_framework import status, generics, permissions, authentication, views
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView

from .serializers import AccountSerializer, RegisterAccountSerializer, LoginSerializer
from django.contrib.auth import login

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterAccountSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
            "Value" : "Created"
            })
        return Response({"Error": "Invalid Credencials"}, status=400)

# Login API
class LoginAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            token = AuthToken.objects.create(user)[1]
            token = token[:8]
            return Response(
                {   "user": AccountSerializer(user, context=self.get_serializer_context()).data,
                    "token": token
                }
            )
        return Response({"Error": "Does Not Exist"}, status=400)

# Verification API
class VerifyTokenView(views.APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get("token")
        try:
            token = AuthToken.objects.get(token_key=token)
        except AuthToken.DoesNotExist:
            return Response({"Valid": False}, status=400)
        return Response({"Valid": True})

# Logout API
class LogoutView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        token = request.data.get("token")
        try:
            token = AuthToken.objects.get(token_key=token)
            token.delete()
        except AuthToken.DoesNotExist:
            return Response({"Deleted": False}, status=400)
        return Response({"Deleted": True})
