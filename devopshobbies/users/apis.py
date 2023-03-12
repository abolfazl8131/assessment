from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (OutPutSerializer , 
    OutPutRegisterSerializer ,
    InputRegisterSerializer , 
    InputUpdateSerializer , 
    OutputUpdateSerializer,)

from rest_framework import serializers
from devopshobbies.users.models import BaseUser , Profile
from devopshobbies.api.mixins import ApiAuthMixin
from devopshobbies.users.selectors import get_profile
from devopshobbies.users.services import register , register_superuser , update

from rest_framework import generics
from drf_spectacular.utils import extend_schema


class ProfileApi(ApiAuthMixin, APIView):

    @extend_schema(responses=OutPutSerializer)
    def get(self, request):
        query = get_profile(user=request.user)
        return Response(OutPutSerializer(query, context={"request":request}).data)
        

class UserUpdateAPI(ApiAuthMixin , generics.UpdateAPIView):

    @extend_schema(request=InputUpdateSerializer, responses=OutputUpdateSerializer)
    def patch(self, request):
        serializer = InputUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = update(
                    email=serializer.validated_data.get("email"),
                    ID = serializer.validated_data.get("ID"),   
                    first_name = serializer.validated_data.get("first_name"),  
                    last_name = serializer.validated_data.get("last_name"),  
            
                    bio=serializer.validated_data.get("bio"),
                    )
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(OutPutRegisterSerializer(user, context={"request":request}).data)


class CreateSuperUserAPI(ApiAuthMixin , generics.CreateAPIView):

     
    @extend_schema(request=InputRegisterSerializer, responses=OutPutRegisterSerializer)
    def post(self, request):
        if not self.request.user.is_admin:
            raise serializers.ValidationError( {
                "status": "failed",
                "message": _("you are not super user"),
            })
        serializer = InputRegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        try:
            user = register_superuser(
                    email=serializer.validated_data.get("email"),
                    ID = serializer.validated_data.get("ID"),   
                    first_name = serializer.validated_data.get("first_name"),  
                    last_name = serializer.validated_data.get("last_name"),  
                    password = serializer.validated_data.get("password"),  
                    bio=serializer.validated_data.get("bio"),
                    )
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(OutPutRegisterSerializer(user, context={"request":request}).data)


class RegisterApi(APIView):

    @extend_schema(request=InputRegisterSerializer, responses=OutPutRegisterSerializer)
    def post(self, request):
        serializer = InputRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = register(
                    email=serializer.validated_data.get("email"),
                    ID = serializer.validated_data.get("ID"),   
                    first_name = serializer.validated_data.get("first_name"),  
                    last_name = serializer.validated_data.get("last_name"),  
                    password=serializer.validated_data.get("password"),
                    bio=serializer.validated_data.get("bio"),
                    )
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(OutPutRegisterSerializer(user, context={"request":request}).data)

