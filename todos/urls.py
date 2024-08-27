from django.urls import path
from todos.api import TodoListCreateView,TodoRetrieveUpdateDestroyView

urlpatterns = [
    path('v1/todo/',TodoListCreateView.as_view(),name="list-create"),
    path('v1/todo/<int:id>/', TodoRetrieveUpdateDestroyView.as_view(),name="get-update-delete"),
]
