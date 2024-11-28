from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

class BloodDonation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    health_status = models.BooleanField(default=True)  # True if in good health
    weight = models.FloatField()
    temperature = models.FloatField()
    blood_type = models.CharField(max_length=10)
    blood_quantity = models.FloatField()
    location = models.CharField(max_length=100)

    def clean(self):
        # Validate age
        if not (18 <= self.age <= 65):
            raise ValidationError("The donor must be between 18 and 65 years old.")
        
        # Validate weight
        if self.weight < 50:
            raise ValidationError("The donor must weigh at least 50 kg.")
        
        # Validate temperature
        if self.temperature > 37:
            raise ValidationError("The temperature must not exceed 37 degrees Celsius.")
        
        # Validate health status
        if not self.health_status:
            raise ValidationError("The donor must be in good health and not suffer from any infectious diseases.")

    def save(self, *args, **kwargs):
        # Call the clean method to validate before saving
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.blood_type}"
