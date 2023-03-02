from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Member


class MemberList(LoginRequiredMixin, ListView):
    model = Member
    template_name = "members/list_member.html"
    context_object_name = "members"


class CreateMember(LoginRequiredMixin, CreateView):
    model = Member
    fields = "__all__"
    template_name = "members/create_member.html"
    success_url = reverse_lazy("list_member")


class UpdateMember(LoginRequiredMixin, UpdateView):
    model = Member
    fields = "__all__"
    template_name = "members/update_member.html"
    success_url = reverse_lazy("list_member")


class DetailMember(LoginRequiredMixin, DetailView):
    model = Member
    template_name = "members/detail_member.html"


class DeleteMember(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = "members/delete_member.html"
    success_url = reverse_lazy("list_member")
