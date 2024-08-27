from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from todos.models import Todo
from todos.serializers import TodoSerializer

import logging

# from opentelemetry import trace

logger = logging.getLogger(__name__)
# tracer = trace.get_tracer(__name__)

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_create(self, serializer) -> None:
        user = self.request.user
        serializer.save(
            user=user,
        )


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
