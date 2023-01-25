from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from thumbnail_maker.fields import ImageWithThumbnailsField


class Login(models.Model):
    username = models.CharField(max_length=100, name="Username")
    password = models.CharField(max_length=100, name="Password")

    def __str__(self):
        return self.username


class PhotoCreate(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to="media/image/", verbose_name='Изображение')
    data_photo = models.DateTimeField(default=timezone.now)
    follow = models.ManyToManyField(User, related_name='create', null=True)

    def total_follow(self):
        return self.follow.count()

    def __str__(self):
        return str(self.author)

    def get_edit_url(self):
        return reverse("media/image/", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse_lazy('my_project', kwargs={'pk': self.pk})


# class Follow(models.Model):
    # author_follow = models.ForeignKey(User, on_delete=models.CASCADE)
    # follow = models.ManyToManyField(User, related_name='create')
    #
    # def __int__(self):
    #     return self.follow


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    # photos_author = models.ImageField(upload_to="media/image/", verbose_name='Изображение')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='detail')

    def __unicode__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('home', kwargs={'post_id': self.pk})
