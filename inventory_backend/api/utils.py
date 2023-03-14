import jwt
from datetime import datetime, timedelta
from django.conf import settings
from api.models import CustomUser
from rest_framework.pagination import PageNumberPagination


def get_access_token(payload, days):
    token = jwt.encode(
        {"exp":datetime.now()+timedelta(days=days), **payload},
        settings.SECRET_KEY,
        algorithm="HS256"
    )
    return token


def decodeJWT(bearer):
    if not bearer:
        return None
    
    token = bearer[7:]

    try:
        decoded = jwt.decode(token, key=settings.SECRET_KEY, algorithm="HS256")
    except Exception:
        return None
    
    if decoded:
        try:
            return CustomUser.objects.get(id=decoded['user_id'])
        except Exception:
            return None
        
class CustomPagination(PageNumberPagination):
    page_size=20
        