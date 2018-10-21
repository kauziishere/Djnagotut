from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_page, name = 'index'),
    path('edu',views.edu_page, name = 'edu'),
    path('skills',views.skills_page, name = 'skills'),
    path('courses',views.courses_page, name = 'courses'),
    path('projects',views.projects_page, name = 'projects'),
]
