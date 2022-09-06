from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    """
    creates a form to add a new review for the movie
    """
    class Meta:
        model = Reviews
        exclude = ('movie', 'posted_by',)
