from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Account

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
        