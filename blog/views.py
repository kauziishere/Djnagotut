from django.shortcuts import render
from .models import Post, Skills
from django.utils import timezone
# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {})
def index_page(request):
	posts = Post.objects.get(title='About me')
	return render(request, 'blog/index.html', {'posts': posts})

def edu_page(request):
	posts = Post.objects.get(title='Education')
	posts.view_count = posts.view_count + 1
	posts.save()
	return render(request, 'blog/edu.html', {'posts': posts})
def courses_page(request):
	posts = Post.objects.get(title='Courses')
	posts.view_count = posts.view_count + 1
	posts.save()
	return render(request, 'blog/courses.html', {'posts': posts})
def projects_page(request):
	posts = Post.objects.get(title='Projects')
	posts.view_count = posts.view_count + 1
	posts.save()
	return render(request, 'blog/projects.html', {'posts': posts})
def skills_page(request):
	posts = Post.objects.get(title='Skills')
	posts.view_count = posts.view_count + 1
	posts.save()
	return render(request, 'blog/skills.html', {'posts': posts})
