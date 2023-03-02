from django.db import models
from django.utils import timezone

from members.models import Member


class Shelf(models.Model):
    number = models.IntegerField()
    floor = models.IntegerField()

    def __str__(self):
        return f"shelf number {self.number} at floor {self.floor}"


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    publisher = models.CharField(max_length=80)
    publish_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned = models.BooleanField(default=False)

    @property
    def is_over_due(self):
        return self.due_date < timezone.now()

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member}"


class Return(models.Model):
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE)
    return_date = models.DateTimeField(auto_now_add=True)
    fine = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.borrow.book.title} returned at: {self.return_date}, fine: {self.fine}"
