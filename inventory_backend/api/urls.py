from django.urls import path, include
from .views import (
    CreateUserView, LoginView, updatePasswordView, MeView, UserActivitesView, UsersView
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register("create-user", CreateUserView, 'create_user')
router.register("login", LoginView, 'login')
router.register("update-password", updatePasswordView, 'update password')
router.register("me", MeView, 'me')
router.register("activities-log", UserActivitesView, 'user activites')
router.register("users", UsersView, 'users')

urlpatterns = [
    path("", include(router.urls))
]

