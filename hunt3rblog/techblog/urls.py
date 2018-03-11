from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name='techblog'
urlpatterns=[
    path('', views.index, name='index'),
    path('topics/<int:pk>/', login_required(views.TopicView.as_view()), name='topic_detail'),
    path('topics/', views.TopicListView.as_view(), name='topic_list'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/comment/', views.comment, name='post_comment'),
    path('logs/', views.LogListView.as_view(), name='log_list')
]

