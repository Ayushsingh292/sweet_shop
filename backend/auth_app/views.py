# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework import status, permissions
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import AllowAny
# from .models import User
# from .serializers import RegisterSerializer, LoginSerializer


# @api_view(["POST"])
# @permission_classes([permissions.AllowAny])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         return Response({"message": "User registered successfully"}, status=201)
#     return Response(serializer.errors, status=400)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     email = request.data.get("email")
#     password = request.data.get("password")

#     if not email or not password:
#         return Response({"error": "Email and password are required."}, status=400)

#     # Authenticate using username field (mapped to email)
#     from django.contrib.auth.models import User
#     try:
#         user_obj = User.objects.get(email=email)
#         username = user_obj.username
#     except User.DoesNotExist:
#         return Response({"error": "Invalid credentials"}, status=401)

#     user = authenticate(username=username, password=password)
#     if user is not None:
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         })
#     else:
#         return Response({"error": "Invalid credentials"}, status=401)

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"message": "User registered successfully"}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email and password are required."}, status=400)

    try:
        user_obj = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=401)

    user = authenticate(request, email=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "email": user.email,
                "name": getattr(user, "name", "")
            }
        })
    else:
        return Response({"error": "Invalid credentials"}, status=401)
