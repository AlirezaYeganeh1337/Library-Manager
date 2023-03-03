from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListMember.as_view(), name="list_member"),
    path("new/", views.CreateMember.as_view(), name="create_member"),
    path(
        "<int:pk>/update/", views.UpdateMember.as_view(), name="update_member"
    ),
    path(
        "<int:pk>/delete/", views.DeleteMember.as_view(), name="delete_member"
    ),
]
