from django.urls import path

from .views import PostListView, PostDetailView, CreatePostView

urlpatterns = [
    path('', PostListView.as_view(), name="index"),
    path('detail/<int:pk>', PostDetailView.as_view(), name="detail" ),
    path('new/', CreatePostView.as_view(), name="newpost"),
]

