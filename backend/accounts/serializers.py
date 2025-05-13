from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        required = True,
        style = {'input_type': 'password'}
    )
    confirm_password = serializers.CharField(
        write_only = True,
        required = True,
        style = {'input_type': 'password'}
    )
    