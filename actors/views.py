from django.shortcuts import render, get_object_or_404
from .models import Actors, Ratings
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from .forms import RatingForm
from django.core.paginator import Paginator


def all_actors(request):
    actors = Actors.objects.all()
    for actor in actors:
        actor.name = str(actor.name).title()
        actor.save()
    paginator = Paginator(actors, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'actors/all_actors.html', {'actors': page_obj})


class AddActor(LoginRequiredMixin, generic.CreateView):
    model = Actors
    fields = ['name', 'surname', 'birthday', 'image', 'Filmweb_rating', 'description', 'movie']
    template_name = 'actors/add_actor.html'
    success_url = reverse_lazy('all_actors')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect('all_actors')


class EditActor(LoginRequiredMixin, generic.UpdateView):
    model = Actors
    template_name = 'actors/edit_actor.html'
    fields = ['name', 'surname', 'birthday', 'image', 'Filmweb_rating', 'description', 'movie']
    success_url = reverse_lazy('all_actors')

    def get_object(self):
        actor = super().get_object()
        if not actor.user == self.request.user:
            raise Http404
        return actor


class DeleteActor(LoginRequiredMixin, generic.DeleteView):
    model = Actors
    template_name = 'actors/delete_actor.html'
    success_url = reverse_lazy('all_actors')

    def get_object(self):
        actor = super().get_object()
        if not actor.user == self.request.user:
            raise Http404
        return actor


class DetailActor(generic.DetailView):
    model = Actors
    template_name = 'actors/detail_actor.html'


def actor_reviews(request, pk):
    actor = get_object_or_404(Actors, pk=pk)
    reviews = Ratings.objects.filter(actor=pk)
    form = RatingForm(request.POST or None)
    if request.method == 'POST':
        rating = form.save(commit=False)
        rating.user = request.user
        rating.actor = actor
        rating.save()
        return render(request, 'actors/actor_reviews.html', {'reviews': reviews, 'form': RatingForm(), 'actor': actor})
    return render(request, 'actors/actor_reviews.html', {'reviews': reviews, 'form': form, 'actor': actor})


class DeleteReview(LoginRequiredMixin, generic.DeleteView):
    model = Ratings
    template_name = 'actors/delete_rating.html'

    def get_object(self):
        review = super().get_object()
        if not review.user == self.request.user:
            raise Http404
        return review

    def get_success_url(self):
        rating = Ratings.objects.get(id=self.kwargs['pk'])
        review_id = rating.actor_id
        return reverse_lazy('actor_reviews', kwargs={'pk': review_id})
