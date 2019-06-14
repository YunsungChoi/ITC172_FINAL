from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre, Review
from .forms import MovieForm, GenreForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'movieapp/index.html')


def getmovies(request):
    movie_list=Movie.objects.all()
    return render(request, 'movieapp/movies.html' ,{'movie_list' : movie_list})

def getreviews(request):
    review_list=Review.objects.all()
    return render(request, 'movieapp/reviews.html', {'review_list': review_list})

def getgenres(request):
    genre_list=Genre.objects.all()
    return render(request, 'movieapp/genres.html', {'genre_list': genre_list})

def moviedetails(request, id):
    mov=get_object_or_404(Movie, pk=id)
    reviews=Review.objects.filter(movie=id).count()
    genre=Genre.objects.all()
    context={
        'mov' : mov,
        'reviews' : reviews,
        'genre' : genre,
    }
    return render(request, 'movieapp/moviedetails.html', context=context)

@login_required
def newMovie(request):
     form=MovieForm
     if request.method=='POST':
          form=MovieForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MovieForm()
     else:
          form=MovieForm()
     return render(request, 'movieapp/newmovie.html', {'form': form})

@login_required
def newGenre(request):
     form=GenreForm
     if request.method=='POST':
          form=GenreForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=GenreForm()
     else:
          form=GenreForm()
     return render(request, 'movieapp/newgenre.html', {'form': form})

def loginmessage(request):
    return render(request, 'movieapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'movieapp/logoutmessage.html')
    