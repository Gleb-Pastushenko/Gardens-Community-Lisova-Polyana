from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'fathers_name', 'birth_date', 'home_address', 'phone_number', 'photo', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise ValidationError(msg)
            else:
                msg = "Unable to login with provided credentials."
                raise ValidationError(msg)
        else:
            msg = "Must provide email and password both."
            raise ValidationError(msg)
        return data