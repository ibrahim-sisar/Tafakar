from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    sender_username = serializers.StringRelatedField(source='sender', read_only=True)
    receiver_username = serializers.StringRelatedField(source='receiver', read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'sender_username', 'receiver_username', 'content', 'timestamp', 'is_read']
        read_only_fields = ['id', 'timestamp', 'is_read', 'sender_username', 'receiver_username']

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
