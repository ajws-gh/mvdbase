from django.shortcuts import render, get_object_or_404
from .models import Movie, Rating
from actors.models import Actors
from django.contrib.auth import authenticate, login
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import RatingForm, UserRegisterForm, Subscribe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.db.models import Q
import urllib
import requests
from django.core.paginator import Paginator
from decouple import config
from django.contrib.auth.models import User
from movies_database.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


YOUTUBE_API_KEY = config('YOUTUBE_API_KEY')


def homepage(request):
    movies = Movie.objects.order_by('-added')[:3]
    actors = Actors.objects.order_by('-added')[:3]

    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            actors = Actors.objects.filter(Q(name__icontains=query) & Q(name__istartswith=query) |
                                           Q(surname__icontains=query) & Q(surname__istartswith=query))
            movies = Movie.objects.filter(
                Q(title__icontains=query) & Q(title__istartswith=query))
            return render(request, 'search_results.html', {'actors': actors, 'movies': movies})

    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = str(sub['Subject'].value())
        message = str(sub['Message'].value())
        from_who = str(sub['Email'].value())
        send_mail(
            subject=subject,
            message=message + f'\n\nReceived from: {from_who}',
            from_email=from_who,
            recipient_list=[EMAIL_HOST_USER],
            fail_silently=False
        )
        return render(request, 'homepage.html',
                      {'form': Subscribe(), 'msg': 'Your message was sent successfully!', 'movies': movies,
                       'actors': actors})

    return render(request, 'homepage.html', {'form': sub, 'msg': None, 'movies': movies, 'actors': actors})


def all_movies(request):
    movies = Movie.objects.all()
    for movie in movies:
        movie.title = str(movie.title).title()
        movie.save()
    paginator = Paginator(movies, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'movies/all_movies.html', {'movies': page_obj})


class AddMovie(LoginRequiredMixin, generic.CreateView):
    model = Movie
    fields = ['title', 'premiere', 'description', 'director', 'IMDB_rating', 'poster', 'duration', 'film_genre',
              'yt_url']
    template_name = 'movies/add_movie.html'
    success_url = reverse_lazy('all_movies')

    def form_valid(self, form):
        try:
            parsed_url = urllib.parse.urlparse(self.request.POST['yt_url'])
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')[0]
            response = requests.get(
                f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={YOUTUBE_API_KEY}')
            json = response.json()
            form.instance.yt_title = json['items'][0]['snippet']['title']
            form.instance.yt_id = video_id
            form.instance.user = self.request.user
            super().form_valid(form)
            return redirect('all_movies')
        except Exception:
            form.instance.user = self.request.user
            super().form_valid(form)
            return redirect('all_movies')


class EditMovie(LoginRequiredMixin, generic.UpdateView):
    model = Movie
    template_name = 'movies/edit_movie.html'
    fields = ['title', 'premiere', 'description', 'director', 'IMDB_rating', 'poster', 'duration', 'film_genre',
              'yt_url']
    success_url = reverse_lazy('all_movies')

    def get_object(self):
        movie = super().get_object()
        if not movie.user == self.request.user:
            raise Http404
        return movie

    def form_valid(self, form):
        try:
            parsed_url = urllib.parse.urlparse(self.request.POST['yt_url'])
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')[0]
            response = requests.get(
                f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={YOUTUBE_API_KEY}')
            json = response.json()
            form.instance.yt_title = json['items'][0]['snippet']['title']
            form.instance.yt_id = video_id
            form.instance.user = self.request.user
            super().form_valid(form)
            return redirect('all_movies')
        except Exception:
            form.instance.user = self.request.user
            super().form_valid(form)
            return redirect('all_movies')


class DeleteMovie(LoginRequiredMixin, generic.DeleteView):
    model = Movie
    template_name = 'movies/delete_movie.html'
    success_url = reverse_lazy('all_movies')

    def get_object(self):
        movie = super().get_object()
        if not movie.user == self.request.user:
            raise Http404
        return movie


class DetailMovie(generic.DetailView):
    model = Movie
    template_name = 'movies/detail_movie.html'

    def get_object(self):
        movie = super().get_object()
        movie.film_genre = Movie.FILM_GENRES[movie.film_genre][1]
        return movie


class SignUp(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('homepage')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


def movie_reviews(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = Rating.objects.filter(movie=pk)
    form = RatingForm(request.POST or None)

    if request.method == 'POST':
        rating = form.save(commit=False)
        rating.user = request.user
        rating.movie = movie
        rating.save()
        return render(request, 'movies/movie_reviews.html', {'reviews': reviews, 'form': RatingForm(), 'movie': movie})
    return render(request, 'movies/movie_reviews.html', {'reviews': reviews, 'form': form, 'movie': movie})


class DeleteReview(LoginRequiredMixin, generic.DeleteView):
    model = Rating
    template_name = 'movies/delete_rating.html'

    def get_object(self):
        review = super().get_object()
        if not review.user == self.request.user:
            raise Http404
        return review

    def get_success_url(self):
        rating = Rating.objects.get(id=self.kwargs['pk'])
        review_id = rating.movie_id
        return reverse_lazy('movie_reviews', kwargs={'pk': review_id})


def user_db(request):
    movies = Movie.objects.filter(user=request.user)
    actors = Actors.objects.filter(user=request.user)
    return render(request, 'user_db.html', {'movies': movies, 'actors': actors})


class DeleteUser(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('homepage')

    def get_object(self):
        user = super().get_object()
        if not user == self.request.user:
            raise Http404
        return user


def video_search(request):
    try:
        searched_term = request.GET['search_term']
        encoded_search_term = urllib.parse.quote(searched_term)
        response = requests.get(
            f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=6&q={encoded_search_term}\
            &type=video&videoEmbeddable=true&key={YOUTUBE_API_KEY}')
        return JsonResponse(response.json())
    except Exception:
        return JsonResponse({'error': 'Not working'})


def top5_movies(request):
    movies = Movie.objects.order_by('-IMDB_rating')[:5]
    return render(request, 'top5_movies.html', {'movies': movies})


def top5_actors(request):
    actors = Actors.objects.order_by('-Filmweb_rating')[:5]
    return render(request, 'top5_actors.html', {'actors': actors})
