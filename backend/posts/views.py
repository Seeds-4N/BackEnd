from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required #로그인시 필요
from accounts.models import User
import json



@method_decorator(csrf_exempt, name= 'dispatch') 
class PostListView(View):
    def get(self, request):
        user_id = request.session.get('user_id')
        if user_id: 
            user = User.objects.get(id=user_id)
            user_posts = Post.objects.filter(author=user)
            serialized_posts = [
                {
                    "author": {"username": post.author.username},
                    "id": post.id,
                    "title": post.title,
                    "content": post.content,
                }
                for post in user_posts
            ]
            return JsonResponse(serialized_posts, safe=False)
        else:
            return JsonResponse({"message": "로그인이 필요합니다."}, status=401)

    def post(self, request):
        params = json.loads(request.body)
        author_username = params.get("author")
        try:
            author = User.objects.get(username=author_username)
        except User.DoesNotExist:
            return JsonResponse({"message": "존재하지 않는 사용자입니다."}, status=400)
        
        post = Post(
            author=author,
            title=params.get("title"),
            content=params.get("content"),
        )
        post.save()
        
        user_id = request.session.get('user')  # 세션에서 사용자 ID 가져오기
        if user_id:
            request.session['post'] = post.id #게시물 id
            request.session['postauthor'] = post.author.id #user.id 와 같음
            return JsonResponse({'message': '저장되었습니다.'},status = 200)
        else:
            return JsonResponse({"message": "로그인이 필요합니다."}, status=401)
        

    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user_id = request.session.get('user_id') 

        if user_id == post.author.id:  # 현재 로그인한 사용자와 게시물 작성자를 비교
            params = json.loads(request.body)
            post.title = params.get("title", post.title)
            post.content = params.get("content", post.content)
            post.save()
            return JsonResponse({'message': '수정되었습니다.'},status = 200)
        else:
            return JsonResponse({"message": "수정 권한이 없습니다."}, status=403)
        

    def delete(self , request , post_id):
        post = get_object_or_404(Post, id=post_id)
        user_id = request.session.get('user_id') 
        if user_id == post.author.id:
            post.delete()
            return JsonResponse({'message': '삭제되었습니다.'},status = 200)
        else:
            return JsonResponse({"message": "삭제 할 수 없습니다."}, status=403)

