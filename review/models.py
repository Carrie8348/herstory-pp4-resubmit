from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie


# Create your models here.
class Reviews(models.Model):
    """
    model for movie reviews
    """

    title = models.CharField(max_length=200, unique=True)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='reviews')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_added",
        null=True)

    class Meta:
        ordering = ['-created_on']

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"Comment {self.body} by {self.title}"
