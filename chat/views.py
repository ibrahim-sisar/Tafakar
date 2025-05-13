from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class MessageViewSet(APIView):


    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        return Response(MessageSerializer(Message.objects.filter(receiver=user), many=True).data)
    
    def post(self, request):        
        user = self.request.user
        data = request.data 
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
