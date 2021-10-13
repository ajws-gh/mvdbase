from django.urls import path
from .views import all_actors, AddActor, EditActor, DeleteActor, DetailActor, actor_reviews, DeleteReview

urlpatterns = [
    path('', all_actors, name='all_actors'),
    path('add_actor', AddActor.as_view(), name='add_actor'),
    path('edit_actor/<int:pk>', EditActor.as_view(), name='edit_actor'),
    path('delete_actor/<int:pk>', DeleteActor.as_view(), name='delete_actor'),
    path('actor_details/<int:pk>', DetailActor.as_view(), name='actor_details'),
    path('actor_reviews/<int:pk>', actor_reviews, name='actor_reviews'),
    path('delete_reviews/<int:pk>', DeleteReview.as_view(), name='delete_reviews'),
]
