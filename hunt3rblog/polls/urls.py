"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from django.conf.urls import url

from . import views

app_name="polls"
urlpatterns = [
    re_path('(?P<question_id>[0-9]+)/vote', views.vote, name='vote'),
    re_path('(?P<questionid>[0-9]+)', views.detail, name='detail'),
    re_path('result', views.result, name='result'),
    re_path('addquestion', views.add_question, name='add_question'),
    re_path('(?P<show_all>all)', views.index, name='index'),
    re_path('', views.index, name='index'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
