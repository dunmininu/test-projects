from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer, UserSerializer
from .models import Todo, User

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["updated"]
    ordering = ["-updated"]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(lookup_field_value)

        self.check_object_permissions(self.request, obj)

        return obj
