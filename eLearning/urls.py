"""eLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from users.views import loginPage, logoutPage
from django.contrib.auth import login, logout
# from registration.backends.default.views import RegistrationView

urlpatterns = [
    path('', user_views.home, name='home'),
    path('about/', user_views.about, name='about'),
    path('contact/', user_views.contact, name='contact'),

    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('forum/', include('forum.urls')),
    path('profile/', include('users.urls')),
    path('login/', loginPage, name='login'),
    path('logout/', logout, name='logout'),
    # path('accounts/', include('django_registration.backends.default.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
