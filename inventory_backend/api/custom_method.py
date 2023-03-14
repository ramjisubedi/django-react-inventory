from rest_framework.permissions import BasePermission

from api.utils import decodeJWT

class IsAuthenticatedCustom(BasePermission):

    def has_premission(self,request, _):
        try:
            auth_token = request.Meta.get("HTTP_AUTHORIZATION",None)
        except Exception:
            return False
        if not auth_token:
            return False
        
        user = decodeJWT(auth_token)

        