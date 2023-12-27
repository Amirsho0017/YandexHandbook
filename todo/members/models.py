from django.db import models


# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255)
    phoneNumber = models.IntegerField(null=True)
    joinedDate = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstName} {self.secondName}"
