from django.urls import path

from .views import PostListView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', PostListView.as_view(), name="index"),
    path('detail/<int:pk>', PostDetailView.as_view(), name="detail" ),
    path('new/', CreatePostView.as_view(), name="newpost"),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('delete/<int:pk>', DeletePostView.as_view(), name="delete"),
]

