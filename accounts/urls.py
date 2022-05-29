from django.urls import path

from .views import (
    UserDashboard,
    UserDocCreatView,
    UserLoginView,
    UserLogoutView,
    UserPassChangeView,
    UserRegisterVerifyCodeView,
    UserRegisterView,
    UserUpdateView,
)

app_name = "accounts"
urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("verify/", UserRegisterVerifyCodeView.as_view(), name="verify"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", UserDashboard.as_view(), name="dashboard"),
    path("pass_change/", UserPassChangeView.as_view(), name="pass_change"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="update"),
    path("doc_update/", UserDocCreatView.as_view(), name="doc"),
]
