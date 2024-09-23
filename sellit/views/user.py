import json
from ..models.user import AppUser
from ..serializers.user_serializers import UserSerializer
from rest_framework.views import APIView, Response, status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework.views import generics
# fro

# @api_view("GET")
# def ping():
#     """return server status"""
#     return "Hello"


class LoginSerializer(TokenObtainPairSerializer):
    pass


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class RegisterView(generics.CreateAPIView):
    
    permission_classes = (AllowAny, )

    def post(self, request):
        """creating a user"""
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.create_user(**serializer.data)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    """User view endpoint"""

    authentication_classes = [JWTAuthentication]
    permission_classes = (AllowAny, )


    def get(self, request, id = None):
        """get all users"""

        users = AppUser.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class UserProfileView(TokenObtainPairView):
    """User Profile View"""

    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, id=None):
        """"""

        data = {}
        if id:
            data = AppUser.objects.get(id=id)
        else:
            data = AppUser.objects.get(id=request.user.id)
        serializer = UserSerializer(data)

        return Response(serializer.data, status=200)
    
    def patch(self, request):
        self.permission_classes = (IsAuthenticated, )

        serializer = UserSerializer(request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
