from django.conf.urls import url
from . import views
urlpatterns = [
    url('', views.index_page, name = 'index'),
    url(r'edu',views.edu_page, name = 'edu'),
    url(r'skills',views.skills_page, name = 'skills'),
    url(r'courses',views.courses_page, name = 'courses'),
    url(r'projects',views.projects_page, name = 'projects'),
]
