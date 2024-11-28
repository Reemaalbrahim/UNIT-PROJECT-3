from django.db import models

# Create your models here.

class ContactUs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)  # Consider using a validation method for phone numbers
    email = models.EmailField()
    blood_type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"