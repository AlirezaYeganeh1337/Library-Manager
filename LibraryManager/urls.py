from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("list_book"))),
    path("admin/", admin.site.urls),
    path("accounts/", include("users.urls")),
    path("members/", include("members.urls")),
    path("library/", include("library.urls")),
]
