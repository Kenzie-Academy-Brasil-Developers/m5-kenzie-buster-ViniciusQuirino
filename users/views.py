from django.shortcuts import render
from rest_framework.views import APIView, Request, Response
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# from .serializers import CustomJWTSerializer


class LoginView(TokenObtainPairView):
    ...


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, 201)
