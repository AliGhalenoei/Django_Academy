from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    phone=serializers.CharField()
    password=serializers.CharField()

class SingupSerializer(serializers.Serializer):
    phone=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    password2=serializers.CharField()

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)

    def validate(self,value):
        if value['password'] and value['password2'] and value['password'] != value['password2']:
            raise serializers.ValidationError('passwords is not mach')
        return value
    
    def validate_phone(self,value):
        
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError('Phone is Alredy')
        return value

    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email is Alredy')
        return value
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('phone','email','password')

        

