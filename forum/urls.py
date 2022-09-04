from django.conf.urls.static import static
from django.urls import path

from eLearning import settings
from . import views as forum_views

urlpatterns = [
    path('', forum_views.forum, name='forum'),
    path('<str:slug>/', forum_views.topic, name='topic'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
