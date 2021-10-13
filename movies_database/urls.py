"""movies_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from movies.views import SignUp, user_db, homepage, video_search, DeleteUser, top5_movies, top5_actors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('movies/', include('movies.urls')),
    path('actors/', include('actors.urls')),
    path('user', user_db, name='user_db'),
    path('delete_user/<int:pk>', DeleteUser.as_view(), name='delete_user'),
    path('video/search', video_search, name='video_search'),
    path('top5_movies', top5_movies, name='top5_movies'),
    path('top5_actors', top5_actors, name='top5_actors'),
    path('search_results', homepage, name='search_results'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('password_reset', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_change', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset_complete', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path(r'session_security/', include('session_security.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
