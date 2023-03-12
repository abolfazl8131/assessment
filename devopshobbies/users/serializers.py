from rest_framework import serializers
from .models import Profile , BaseUser
from .validators import number_validator, special_char_validator, letter_validator
from django.core.validators import MinLengthValidator
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken



class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = BaseUser

            fields = ("ID", "first_name", "last_name", "email")

class OutPutSerializer(serializers.ModelSerializer):
    user =  UserSerializer()
    class Meta:
        model = Profile 
        fields = ('user',"bio", "posts_count", "subscriber_count", "subscription_count")

class InputRegisterSerializer(serializers.Serializer):

        email = serializers.EmailField(max_length=255)
        bio = serializers.CharField(max_length=1000, required=False)
        ID = serializers.CharField(max_length=10)
        first_name = serializers.CharField(max_length = 100)
        last_name = serializers.CharField(max_length = 100)

        password = serializers.CharField(
                validators=[
                        number_validator,
                        letter_validator,
                        special_char_validator,
                        MinLengthValidator(limit_value=10)
                    ]
                )

        confirm_password = serializers.CharField(max_length=255)

        def validate_ID(self , ID):
            if not ID.isnumeric():
                raise serializers.ValidationError("ID must be numeric")
            return ID
        
        def validate_email(self, email):
            if BaseUser.objects.filter(email=email).exists():
                raise serializers.ValidationError("email Already Taken")
            return email

        def validate(self, data):
            if not data.get("password") or not data.get("confirm_password"):
                raise serializers.ValidationError("Please fill password and confirm password")
            
            if data.get("password") != data.get("confirm_password"):
                raise serializers.ValidationError("confirm password is not equal to password")
            return data

class InputUpdateSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=255)
        bio = serializers.CharField(max_length=1000, required=False)
        ID = serializers.CharField(max_length=10)
        first_name = serializers.CharField(max_length = 100)
        last_name = serializers.CharField(max_length = 100)


        def validate_ID(self , ID):
            if not ID.isnumeric():
                raise serializers.ValidationError("ID must be numeric")
            return ID
        
        def validate_email(self, email):
            if BaseUser.objects.filter(email=email).exists():
                raise serializers.ValidationError("email Already Taken")
            return email


class OutputUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ("email", "ID","first_name", "last_name", "created_at", "updated_at")

class OutPutRegisterSerializer(serializers.ModelSerializer):

        token = serializers.SerializerMethodField("get_token")

        class Meta:
            model = BaseUser 
            fields = ("email", "ID","first_name", "last_name", "token", "created_at", "updated_at")

        def get_token(self, user):
            data = dict()
            token_class = RefreshToken

            refresh = token_class.for_user(user)

            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

            return data


