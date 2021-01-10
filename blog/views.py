from django.shortcuts import render, get_object_or_404,redirect
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #  login_required for create a new post
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.


def home(request):
    keyword = request.GET.get("keyword")
    if keyword:
        posts = Post.object.filter(title__contains = keyword)
        context = {
            posts:"posts",
        }
        return render(request,"blog/home.html",context)

    posts = Post.objects.all()
    return render(request,"blog/home.html",{"posts":posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html --> part of the urls.py
    context_object_name = 'posts' # posts explained early stage in our list
    ordering = ['-created_date'] # I sort the posts by date
    paginate_by=4

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html --> part of the urls.py
    context_object_name = 'posts' # posts explained early stage in our list
    paginate_by=4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created_date')

class CityPostListView(ListView):
    model = Post
    template_name = 'blog/city_posts.html' #<app>/<model>_<viewtype>.html --> part of the urls.py
    context_object_name = 'posts' # posts explained early stage in our list
    paginate_by=4

    def get_queryset(self):
        city = get_object_or_404(Post, username=self.kwargs.get('city'))
        return Post.objects.filter(city=city).order_by('-created_date')

class PostDetailView(DetailView):
    model =  Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content','post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
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


