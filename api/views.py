from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from  rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        print(user.username)
        return Response({'token': token.key, 'id': token.user_id, 'user':user.username})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(id=1)
    serializer_class = UserSerializer



class IndexViewSet(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    def get(self,request, format=None):
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        response = {'data': serializer.data}
        return Response(response)
            
    def post(self, request, format=None):
        serializer=UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)   
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



