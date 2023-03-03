from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "password-change/",
        views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change-done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
