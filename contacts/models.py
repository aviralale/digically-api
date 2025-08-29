from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=56)
    email_address = models.EmailField()
    company_name = models.CharField(max_length=100)
    service_needed = models.CharField(max_length=100)
    budget_range = models.CharField(max_length=100)
    project_details = models.TextField()

    def __str__(self):
        return f" Inquired by {self.full_name}"
