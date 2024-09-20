from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView

# Create your views here.
class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        user = request.body
        