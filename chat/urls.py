from django.urls import path
from .views import *

urlpatterns = [
    path("", MessageViewSet.as_view(), name="message-list"),
]
