from django import forms
from .widgets import CustomClearableFileInput
from .models import Movie
from cloudinary.models import CloudinaryField



class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

    featured_image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        movies = Movie.objects.all()

       
