from django.db import models
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField("email",null=True,blank=True)
    address = models.CharField(max_length=255,default="unknown")

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})
    
    def get_update_url(self):
        return reverse("update",kwargs={"pk":self.id})

    def get_delete_url(self):
        return reverse("delete-contact",kwargs={"pk":self.id})
    
    class Meta:
        ordering = ['full_name','relation']