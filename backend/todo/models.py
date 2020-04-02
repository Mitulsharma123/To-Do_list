from django.db import models

class Todo(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("last name", max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    description = models.DateField("created at", auto_now_add=True)

    def _str_(self):
        return self.first_name