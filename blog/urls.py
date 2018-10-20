from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_page, name = 'index'),
    path(r'edu',views.edu_page, name = 'edu'),
    path(r'skills',views.skills_page, name = 'skills'),
    path(r'courses',views.courses_page, name = 'courses'),
    path(r'projects',views.projects_page, name = 'projects'),
]
