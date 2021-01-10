from django.urls import path
from . import views
from users import views as user_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CityPostListView



urlpatterns = [
    path('', PostListView.as_view(),name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(),name="user-posts"),
    path('city/<str:city>', UserPostListView.as_view(),name="city-posts"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/create/', PostCreateView.as_view(), name="post-create"),
    path('register/', user_views.register, name="register"),


]