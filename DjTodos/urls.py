from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("todos.urls")),
    path('api/', include("contacts.urls")),
    path('swagger/', include("swagger.urls")),
    
    # should always be last
    path('', include("vite_integration.urls")),


]
