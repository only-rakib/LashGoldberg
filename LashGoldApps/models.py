from django.db import models
from django.urls import reverse


class Office_Address(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=150, )
    address2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50,)
    zip_code = models.CharField(max_length=50,)
    phone = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    cover_pic = models.ImageField(
        upload_to='images/', help_text='Enter Company Office Pic')

    def get_absolute_url(self):
        return reverse("offices_inside", kwargs={'pk': str(self.id), 'office_title': self.title})

    def __str__(self):
        return self.title

