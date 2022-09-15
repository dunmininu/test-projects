from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from todo.views import UserViewSet, TodoView
from todo.auth.api import LoginViewSet, RegisterViewSet, RefreshViewSet


routes = SimpleRouter()

# Authentication

routes.register(r"auth/login", LoginViewSet, basename="auth-login")
routes.register(r"auth/register", RegisterViewSet, basename="auth-register")
routes.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")
routes.register(r"todos", TodoView, "todo")


# user

routes.register(r"user", UserViewSet, basename="user")


urlpatterns = [*routes.urls]
