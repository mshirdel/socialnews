from django.urls import path
from . import views

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.UserList.as_view()),
    path("user/", views.UpdateUser.as_view()),
    path("user/<int:pk>/", views.UserInfo.as_view()),
    path("register/", views.RegisterUser.as_view()),
    path("login/", views.LoginUser.as_view()),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
