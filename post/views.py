from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post
from django.http import JsonResponse
from .serializers import PostSerializer

# Create your views here.
class PostView(APIView):
    def get(self, request):
        posts   = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
        