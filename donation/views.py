from re import template
from unicodedata import category
from attr import attrs, fields
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    
)
from . models import Post, Category
from .forms import PostForm
# from eWasteM import eWasteManagementChecker


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'donation/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'donation/home.html'  
    fields = ['title', 'category', 'content', 'image', 'location']
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
class UserPostListView(ListView):
    model = Post
    template_name = 'donation/user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # check=eWasteManagementChecker.CheckImage("img.png")
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
  

def about(request):
    return render(request, 'donation/about.html', {'title': 'About'})

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'donation/add_post.html'


