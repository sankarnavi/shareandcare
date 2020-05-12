
from django.conf import settings
from django.db import models
from django.contrib.admin import options
from django.contrib.auth.models import User
from product.models import Products
from django.urls import reverse

STATUS = (
    (1, 'Accepted'),
    (0, 'Declined'),
    (69, 'Pending')
)


class Contact(models.Model):
    Requester = models.OneToOneField(User, on_delete=models.CASCADE)

    status = models.PositiveSmallIntegerField(choices=STATUS, default=69)

    JobtaskID = models.ForeignKey(Products, on_delete=models.CASCADE)

    Approver = models.EmailField(max_length=254)

    def __str__(self):
        return self.Requester.username

    def get_absolute_url(self):
        return reverse('Accept', kwargs={
            'id': self.id
        })

    def get_absolute_urls(self):
        return reverse('Reject', kwargs={
            'id': self.id
        })
