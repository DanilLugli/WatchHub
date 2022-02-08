from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Maison(models.Model):
    maison = models.CharField(max_length=20, default=None)

    def __str__(self):
        return f'{self.maison}'

class Condition(models.Model):
    condition = models.CharField(max_length=20, default='New')

    def get_absolute_url(self):
        return reverse('blog:blogPostDetail', args=(str(self.id)))
        #return reverse('Watch-Hub-Home')

    def __str__(self):
        return f'{self.condition}'


class Watch(models.Model):
    maison = models.ForeignKey(Maison, default=None, on_delete=models.CASCADE)
    model = models.CharField(max_length=40, default='')
    reference = models.CharField(max_length=40, default='')
    movement = models.CharField(max_length=40, default='')
    condition = models.CharField(max_length=20, default='New')
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    date_creation = models.DateField(null=True)
    photo = models.ImageField(default='watch_cover_default', upload_to='static/image/')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return f'{self.model} - {self.pk}'

    def get_absolute_url(self):
        return reverse('blog:blogPostDetail', args=(str(self.id)))
        #return reverse('Watch-Hub-Home')