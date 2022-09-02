from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from movie.models import Movie
from .models import Reviews
from .forms import ReviewForm


@login_required
def add_review(request, movie_id):
    """
    view to add reviews to the database
    """

    if request.method == 'POST':
    
        movie = get_object_or_404(Movie.objects.all(), pk=movie_id)
        print(movie)        
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.posted_by = request.user
            form.instance.movie = movie
            form.save()
            messages.success(request, 'review Added')
            return redirect(reverse('home',))
        else:
            messages.error(
                request,
                'The review was not added. Please check the form is valid.'
            )
    else:
        form = ReviewForm()

    template = 'review/add_reviews.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """
    view to edit review in the db
    """

    review = get_object_or_404(Reviews.objects.all(), pk=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'review was updated')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'review was not updated please'
                ' check the form is valid'
            )
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.title}')

    template = 'review/edit_reviews.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)
    



@login_required
def delete_review(request, review_id):
    """ Delete a review """

    review = get_object_or_404(Reviews, pk=review_id)
    review.delete()
    messages.success(request, f'{review.title} deleted!')
    return redirect(reverse('home'))