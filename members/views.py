from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from LibraryManager.utils import dynamic_query

from .models import Member


class ListMember(LoginRequiredMixin, ListView):
    model = Member
    template_name = "members/list_member.html"
    context_object_name = "members"

    def get_queryset(self):
        model_fields = [field.name for field in self.model._meta.fields]

        return self.model.objects.all().filter(
            **dynamic_query(self.request.GET.items(), model_fields)
        )


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


class DeleteMember(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = "members/delete_member.html"
    success_url = reverse_lazy("list_member")
