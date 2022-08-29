from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    director = models.CharField(max_length=300)
    lead_actor = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    updated_on = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    released_on = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='movie_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='movie_dislikes', blank=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Review {self.body} by {self.name}"
