from django.db import models


class Member(models.Model):
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
