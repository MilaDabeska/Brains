from django.conf.urls.static import static
from django.urls import path

from eLearning import settings
from . import views as user_views
from .views import loginPage, logoutPage

urlpatterns = [
    path('', user_views.profile, name='profile'),
    path('student/', user_views.student, name='student'),
    path('professor/', user_views.professor, name='professor'),

    path('admin/', user_views.admin, name='admin'),
    path('edit/<str:username>/', user_views.update_user, name='update_user'),
    path('delete/<str:username>/', user_views.delete_user, name='delete_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
