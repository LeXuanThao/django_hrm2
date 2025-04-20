from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class LoginApiView(APIView):
    # Login with email and password over JWT
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        user_serializer = UserSerializer(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user_serializer.data
        })