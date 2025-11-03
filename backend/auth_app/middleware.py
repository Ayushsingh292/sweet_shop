from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from auth_app.models import User  # your MongoEngine User model

class MongoJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None
        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None
        validated_token = self.get_validated_token(raw_token)
        try:
            user_id = validated_token.get("user_id")
            user = User.objects.get(id=user_id)
            return (user, validated_token)
        except Exception:
            raise AuthenticationFailed("Invalid or expired token")
