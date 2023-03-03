from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Book, Borrow, Category, Return, Shelf
from LibraryManager.utils import dynamic_query


class CreateShelf(LoginRequiredMixin, CreateView):
    model = Shelf
    fields = "__all__"
    template_name = "library/shelf/create_shelf.html"
    success_url = reverse_lazy("list_shelf")


class DetailShelf(LoginRequiredMixin, DetailView):
    model = Shelf
    template_name = "library/shelf/detail_shelf.html"


class ListShelf(LoginRequiredMixin, ListView):
    model = Shelf
    context_object_name = "shelves"
    template_name = "library/shelf/list_shelf.html"

    def get_queryset(self):
        model_fields = [field.name for field in self.model._meta.fields]
        return self.model.objects.all().filter(
            **dynamic_query(self.request.GET.items(), model_fields)
        )


class UpdateShelf(LoginRequiredMixin, UpdateView):
    model = Shelf
    template_name = "library/shelf/update_shelf.html"
    fields = "__all__"
    success_url = reverse_lazy("list_shelf")


class DeleteShelf(LoginRequiredMixin, DeleteView):
    model = Shelf
    template_name = "library/shelf/delete_shelf.html"
    success_url = reverse_lazy("list_shelf")


class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    fields = "__all__"
    template_name = "library/category/create_category.html"
    success_url = reverse_lazy("list_category")


class DetailCategory(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "library/category/detail_category.html"


class ListCategory(ListView):
    model = Category
    context_object_name = "categories"
    template_name = "library/category/list_categories.html"

    def get_queryset(self):
        model_fields = [field.name for field in self.model._meta.fields]
        return self.model.objects.all().filter(
            **dynamic_query(self.request.GET.items(), model_fields)
        )


class UpdateCategory(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "library/category/update_category.html"
    fields = "__all__"
    success_url = reverse_lazy("list_category")


class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "library/category/delete_category.html"
    success_url = reverse_lazy("list_category")


class CreateBook(LoginRequiredMixin, CreateView):
    model = Book
    fields = "__all__"
    template_name = "library/book/create_book.html"
    success_url = reverse_lazy("list_book")


class DetailBook(DetailView):
    model = Book
    template_name = "library/book/detail_book.html"


class ListBook(ListView):
    model = Book
    context_object_name = "books"
    template_name = "library/book/list_book.html"

    def get_queryset(self):
        model_fields = [
            f"{field.name}__name" if field.name == "category" else field.name for field in self.model._meta.fields
        ]
        model_fields.remove("shelf")
        model_fields.append("shelf__number")
        qp = dict()

        for key, value in self.request.GET.items():
            if key == "category":
                qp[f"{key}__name"] = value
                continue
            elif key == "shelf":
                qp[f"{key}__number"] = value
                continue
            else:
                qp[key] = value
        print(dynamic_query(qp.items(), model_fields))
        return self.model.objects.all().filter(
            **dynamic_query(qp.items(), model_fields)
        )


class UpdateBook(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "library/book/update_book.html"
    fields = "__all__"
    success_url = reverse_lazy("list_book")


class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "library/book/delete_book.html"
    success_url = reverse_lazy("list_book")


class CreateBorrow(LoginRequiredMixin, CreateView):
    model = Borrow
    fields = ["member", "book", "due_date"]
    template_name = "library/borrow/create_borrow.html"
    success_url = reverse_lazy("list_borrow")

    def form_valid(self, form):
        book = form.cleaned_data.get("book")
        if not book.is_available:
            return HttpResponse("not available")
        self.object = form.save()
        book.is_available = False
        book.save()
        return HttpResponseRedirect(self.get_success_url())


class DetailBorrow(LoginRequiredMixin, DetailView):
    model = Borrow
    template_name = "library/borrow/detail_borrow.html"


class ListBorrow(LoginRequiredMixin, ListView):
    model = Borrow
    context_object_name = "borrows"
    template_name = "library/borrow/list_borrow.html"
    success_url = "/"

    def get_queryset(self):
        model_fields = ["book__title", "member__firstName", "member__lastName"]
        return self.model.objects.all().filter(
            **dynamic_query(self.request.GET.items(), model_fields)
        )


class UpdateBorrow(LoginRequiredMixin, UpdateView):
    model = Borrow
    template_name = "library/borrow/update_borrow.html"
    fields = "__all__"
    success_url = reverse_lazy("list_borrow")


class DeleteBorrow(LoginRequiredMixin, DeleteView):
    model = Borrow
    template_name = "library/borrow/delete_borrow.html"
    success_url = reverse_lazy("list_borrow")


class CreateReturn(LoginRequiredMixin, CreateView):
    model = Return
    fields = "__all__"
    template_name = "library/return/create_return.html"
    success_url = reverse_lazy("list_return")

    def form_valid(self, form):
        borrow = form.cleaned_data.get("borrow")
        book = borrow.book
        if borrow.returned:
            return HttpResponse("already returned")
        borrow.returned = True
        borrow.save()
        book.is_available = True
        book.save()
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class DetailReturn(LoginRequiredMixin, DetailView):
    model = Return
    template_name = "library/return/detail_return.html"


class ListReturn(LoginRequiredMixin, ListView):
    model = Return
    context_object_name = "returns"
    template_name = "library/return/list_return.html"

    def get_queryset(self):
        model_fields = ["borrow__book__title", "borrow__member__firstName", "borrow__member__lastName"]
        return self.model.objects.all().filter(
            **dynamic_query(self.request.GET.items(), model_fields)
        )


class UpdateReturn(LoginRequiredMixin, UpdateView):
    model = Return
    template_name = "library/return/update_return.html"
    fields = "__all__"
    success_url = reverse_lazy("list_return")


class DeleteReturn(LoginRequiredMixin, DeleteView):
    model = Return
    template_name = "library/return/delete_return.html"
    success_url = reverse_lazy("list_return")
