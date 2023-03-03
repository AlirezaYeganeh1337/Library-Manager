from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse_lazy("list_book")


class ChangePassword(PasswordChangeView):
    template_name = "users/password_change.html"

    def get_success_url(self):
        return reverse_lazy("login")
