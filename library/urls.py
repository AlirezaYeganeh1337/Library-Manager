from django.urls import path

from . import views

urlpatterns = [
    path("shelf/new/", views.CreateShelf.as_view(), name="create_shelf"),
    path("shelf/<int:pk>/", views.DetailShelf.as_view(), name="retrieve_shelf"),
    path("shelf/", views.ListShelf.as_view(), name="list_shelf"),
    path(
        "shelf/<int:pk>/update/",
        views.UpdateShelf.as_view(),
        name="update_shelf",
    ),
    path(
        "shelf/<int:pk>/delete/",
        views.DeleteShelf.as_view(),
        name="delete_shelf",
    ),
    path(
        "category/new/", views.CreateCategory.as_view(), name="create_category"
    ),
    path(
        "category/<int:pk>/",
        views.DetailCategory.as_view(),
        name="retrieve_category",
    ),
    path("category/", views.ListCategory.as_view(), name="list_category"),
    path(
        "category/<int:pk>/update/",
        views.UpdateCategory.as_view(),
        name="update_category",
    ),
    path(
        "category/<int:pk>/delete/",
        views.DeleteCategory.as_view(),
        name="delete_category",
    ),
    path("book/new/", views.CreateBook.as_view(), name="create_book"),
    path("book/<int:pk>/", views.DetailBook.as_view(), name="retrieve_book"),
    path("book/", views.ListBook.as_view(), name="list_book"),
    path(
        "book/<int:pk>/update/", views.UpdateBook.as_view(), name="update_book"
    ),
    path(
        "book/<int:pk>/delete/", views.DeleteBook.as_view(), name="delete_book"
    ),
    path("borrow/new/", views.CreateBorrow.as_view(), name="create_borrow"),
    path(
        "borrow/<int:pk>/", views.DetailBorrow.as_view(), name="retrieve_borrow"
    ),
    path("borrow/", views.ListBorrow.as_view(), name="list_borrow"),
    path(
        "borrow/<int:pk>/update/",
        views.UpdateBorrow.as_view(),
        name="update_borrow",
    ),
    path(
        "borrow/<int:pk>/delete/",
        views.DeleteBorrow.as_view(),
        name="delete_borrow",
    ),
    path("return/new/", views.CreateReturn.as_view(), name="create_return"),
    path(
        "return/<int:pk>/", views.DetailReturn.as_view(), name="retrieve_return"
    ),
    path("return/", views.ListReturn.as_view(), name="list_return"),
    path(
        "return/<int:pk>/update/",
        views.UpdateReturn.as_view(),
        name="update_return",
    ),
    path(
        "return/<int:pk>/delete/",
        views.DeleteReturn.as_view(),
        name="delete_return",
    ),
]
