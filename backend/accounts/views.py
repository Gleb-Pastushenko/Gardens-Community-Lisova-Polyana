from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import User
from .serializers import UserSerializer, LoginSerializer

# реєстрація нових користувачів
class Register(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# вхід користувачів
class Login(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response({
            "user": UserSerializer(user).data, 
            "token": user.auth_token
        })