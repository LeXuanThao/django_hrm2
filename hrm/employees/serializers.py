from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import (
    make_password
)
from .models import Employee, Account

class LoginSerializer(serializers.Serializer):
    # Login throw email and password
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials")
            attrs['user'] = user
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")
        return attrs

class EmployeeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'avatar', 'is_active']
                  
class EmployeeSerializer(serializers.ModelSerializer):
    account = EmployeeAccountSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': True},
            'account': {'required': False}
        }

class AccountEmployeeCreateSerializer(serializers.ModelSerializer):
    # Create account for employee
    class Meta:
        model = Account
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def create(self, validated_data):
        # Hash the password
        password = validated_data.pop('password')
        validated_data['is_active'] = True
        validated_data['is_staff'] = False
        validated_data['is_superuser'] = False
        validated_data['password'] = make_password(password)
        account = Account.objects.create_user(**validated_data)
        return account
class EmployeeCreateSerializer(serializers.ModelSerializer):
    account = AccountEmployeeCreateSerializer()

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        account = AccountEmployeeCreateSerializer.create(AccountEmployeeCreateSerializer(), validated_data=account_data)
        employee = Employee.objects.create(account=account, **validated_data)
        return employee
    
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': True},
            'account': {'required': False}
        }