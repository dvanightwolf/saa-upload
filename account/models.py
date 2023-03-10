from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager


class Profile(AbstractUser):
    # Holds the user's bio
    bio = models.CharField(max_length=300, blank=True, null=True)


class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    post_photo = models.ImageField(upload_to="Article/", blank=False, null=False,
                                   default="saa_logo.png")
    tags = TaggableManager()
    video_url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('article_details', args=[self.pk, self.slug])

    def __str__(self):
        return self.title


class ArticleContent(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, blank=False)
    article_text = models.TextField()
    photo = models.ImageField(upload_to="article/", blank=True, null=False)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.article.title + "__" + self.comment


class Slide(models.Model):
    photo_1 = models.ImageField(upload_to="slide/", default="SAA_logo.png", blank=False, null=False)
    photo_2 = models.ImageField(upload_to="slide/", default="SAA_logo.png", blank=False, null=False)
    photo_3 = models.ImageField(upload_to="slide/", default="SAA_logo.png", blank=False, null=False)
    photo_4 = models.ImageField(upload_to="slide/", default="SAA_logo.png", blank=False, null=False)


class Gallery(models.Model):
    moon_photo = models.ImageField(upload_to="gallery/moon/", default="SAA_logo.png", blank=False, null=False)
    sun_photo = models.ImageField(upload_to="gallery/photo/", default="SAA_logo.png", blank=False, null=False)

    def __str__(self):
        return str(self.id)
