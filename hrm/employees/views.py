from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer, EmployeeSerializer, EmployeeCreateSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Employee

# Create your views here.
class LoginApiView(APIView):
    # Login with email and password over JWT
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })
    
class ListEmployeeApiView(APIView):
    # List all employees
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)