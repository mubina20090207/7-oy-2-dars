from django.urls import path
from .views import *

urlpatterns = [
    # home
    path('', index, name='index'),

    # course
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('course/<int:course_id>/update/', updateCourse, name='updateCourse'),
    path('course/<int:course_id>/delete/', deleteCourse, name='deleteCourse'),
    path('course/add/', addCourse, name='addCourse'),

    # student
    path('student/<int:student_id>/', student_detail, name='student_detail'),

    # auth
    path('auth/register/', register, name='register'),
    path('auth/login/', loginView, name='login'),
    path('auth/logout/', logoutView, name='logout'),

    # not found
    path('not-found/', not_found, name='not_found'),

    # settings
    path('settings/', settings, name='settings'),
    path('settings/save/', settings, name='settings_save'),
    path('settings/photo/delete/', remove_picture, name='remove_picture'),
    path('settings/delete-account/', delete_account, name='delete_account'),
    path('settings/delete-account/confirm/', delete_account_confirm, name='delete_account_confirm'),
]
