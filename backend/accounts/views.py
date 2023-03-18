import json
from django.shortcuts import render ,redirect
from django.core import serializers
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


from .serializers import UserCreateSerializer
from .serializers import UserLoginSerializer
from .models import User



@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(email=serializer.validated_data['email']).first() is None:
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'success': 'True',
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def userlist(request):
    if request.method == 'GET':
        users_list = serializers.serialize("json", User.objects.all())
        return Response(json.loads(users_list), content_type="json", status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def ForgotEmailView(request):
    if request.method == 'POST':
        getEmail = request.data["email"] # 포스트에서 email 값 가져오기
        # 도전
        try:
            # 성공
            user = User.objects.get(email=getEmail) # 유저 모델에서 유저 객체 가져오기
            return Response({'email': user.email}, status=status.HTTP_200_OK) # 유저 모델 email 출력
        except:
            # 실패
            return Response({'message': 'fail'}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
@permission_classes([AllowAny])
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST) 
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 중요!
            messages.success(request, 'Your password was successfully updated!')
            return Response(status=status.HTTP_200_OK)
        else:
            messages.error(request, 'Please correct the error below.')
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        form = PasswordChangeForm(request.user)
    return Response(status=status.HTTP_205_RESET_CONTENT)

@api_view(['POST'])
@permission_classes([AllowAny])
def logout(request):
    auth.logout(request)
    return Response(status=status.HTTP_200_OK)
