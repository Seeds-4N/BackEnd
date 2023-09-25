from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Folder
from accounts.models import User
from place.models import Places
from rest_framework.views import APIView

import json

class save_folders(APIView):
    def post(self , request):
        user_id =  request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        params = request.data
        folders = Folder(
            title = params.get('title'),
            user = user)
        folders.save()
        return JsonResponse({"message" : "저장 되었습니다."}, status=200)
        
        

        
