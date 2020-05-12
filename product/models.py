from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORY_CHOICES = (
    ('Food', 'Food'),
    ('Clothes', 'Clothes'),
    ('Others', 'Others')
)
STATUS = (
    (1, 'Completed'),
    (0, 'Inprogress'),
    (69, 'Cancelled')
)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Products(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics', null=True,)
    desc = models.TextField()
    postedon = models.DateField(auto_now=True)
    expiry = models.DateField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    Status = models.PositiveSmallIntegerField(choices=STATUS, default=0)
    Editor1 = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Productdetails', kwargs={
            'id': self.id,
        })

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)
