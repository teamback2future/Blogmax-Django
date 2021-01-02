from django.urls import path
from . import views
from users import views as user_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView



urlpatterns = [
    path('', PostListView.as_view(),name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(),name="user-posts"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/create/', PostCreateView.as_view(), name="post-create"),
    path('register/', user_views.register, name="register"),
    path('about/', views.about,name="blog-about"),
    path('contact/', views.contact,name="blog-contact"),
    path('post/<int:pk>/comment/', views.addComment, name="comment"),

]