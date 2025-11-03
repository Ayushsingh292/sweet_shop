from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Sweet Shop API is running 🚀"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth_app.urls')),   
    path('api/sweets/', include('sweets.urls')),   
]

