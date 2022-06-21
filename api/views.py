from rest_framework import generics, permissions
from .serializers import TodoSerializer, TodoCompleteSerializer
from todo.models import Todo
from django.utils import timezone


class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    #User has to be logged in, and only sees objects for the loggen in user.
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')

class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    #User has to be logged in, and only sees objects for the loggen in user.
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    #User has to be logged in, and only sees objects for the loggen in user.
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoComplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    #User has to be logged in, and only sees objects for the loggen in user.
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(sself, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()