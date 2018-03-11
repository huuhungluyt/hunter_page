from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

from .utils import get_client_ip, log_comment
from .models import Post, Topic, Comment, Log
from .forms import CommentForm
# from .tables import LogTable
# from table.views import FeedDataView



# @login_required
def index(request):
    lastest_topics= Topic.objects.order_by('-time_created')[:4]
    lastest_posts= Post.objects.order_by('-time_created')[:3]
    template= loader.get_template('techblog/index.html')
    content={
        'lastest_topics': lastest_topics,
        'lastest_posts': lastest_posts,
    }
    return HttpResponse(template.render(content, request))


class TopicView(generic.DetailView):
    model= Topic

class PostView(generic.DetailView):
    model=Post
    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['form'] = CommentForm
        return context


class TopicListView(generic.ListView):
    model = Topic

class PostListView(generic.ListView):
    model = Post



def comment(request, post_id):
    post_obj=get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        form= CommentForm(request.POST)
        if form.is_valid():
            comment_content= form.cleaned_data['content']
            if comment_content:
                reader= User.objects.first()
                c= Comment(post=post_obj,content=comment_content, reader=reader)
                c.save()
                log_comment(request, reader, comment_content)
                
            # else:
            #     return render(request, 'polls/error.html', {'pre_link': '/polls'})
    return HttpResponseRedirect(reverse('techblog:post_detail', args=(post_id,)))


# def display_logs(request):
#     log_table= LogTable()
#     return render(request, 'techblog/logs.html', {'log_table': log_table})

class LogListView(generic.ListView):
    model=Log