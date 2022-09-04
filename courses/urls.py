from django.conf.urls.static import static
from django.urls import path

from eLearning import settings
from courses import views as course_views
from users import views as user_views

urlpatterns = [
    path('', course_views.courses, name='courses'),

    path('student/<str:course_name>/', user_views.course_homepage, name='course_homepage'),
    path('student/<str:course_name>/<slug>', user_views.student_course,
         name='student_course'),

    path('professor/<str:course_name>/', course_views.course, name='professor_course'),
    path('professor/<str:course_name>/delete/', course_views.delete_course, name='delete'),
    path('professor/<str:course_name>/edit/', course_views.update_course, name='edit'),

    path('professor/<str:course_name>/students/', course_views.list_students, name='list_students'),
    path('professor/<str:course_name>/students/<int:student_id>/remove/',
         course_views.remove_students, name='remove_students'),
    path('professor/<str:course_name>/students/<int:student_id>/add/',
         course_views.add_students, name='add_students'),

    path('professor/<str:course_name>/<str:slug>/', course_views.chapter, name='chapter'),
    path('professor/edit/<str:course_name>/<str:slug>/',
         course_views.update_chapter, name='edit_chapter'),
    path('professor/delete/<str:course_name>/<str:slug>/',
         course_views.delete_chapter, name='delete_chapter'),

    path('professor/<str:course_name><str:slug>/<int:txt_id>/txt/edit/',
         course_views.update_text_block, name='edit_txt'),
    path('professor/txt/delete/<int:txt_id>/', course_views.delete_text_block, name='delete_txt'),

    path('professor/<str:course_name>/<str:slug>/<int:yt_id>/link/edit/',
         course_views.update_yt_link, name='edit_link'),
    path('professor/link/delete/<int:yt_id>/', course_views.delete_yt_link, name='delete_link'),

    path('professor/file/delete/<int:file_id>/', course_views.delete_file, name='delete_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
