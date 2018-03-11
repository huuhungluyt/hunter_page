from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.utils import timezone

# Create your views here.
from .forms import AddQuestionForm, AddChoiceForm, VoteForm
from .models import Question, Choice

# def index(request):
#     top_question= Question.objects.order_by('-pub_date')[:5]
#     result= ', <br>'.join([q.question_text for q in top_question])
#     return HttpResponse(result)

def index(request, show_all="abc"):
    if show_all == "all" :
        all_question= Question.objects.all()
        context={
            'all_question': all_question
        }
    else :
        top_question= Question.objects.order_by('-pub_date')[:5]
        context={
            'top_question': top_question
        }
    template = loader.get_template('polls/index.html')
    
    return HttpResponse(template.render(context, request))

def detail(request, questionid):
    question= get_object_or_404(Question,id=questionid)
    template= loader.get_template('polls/question_detail.html')
    context={
        'question_object': question,
    }
    return HttpResponse(template.render(context, request))

def add_question(request):
    if request.method=='POST':
        form= AddQuestionForm(request.POST)
        if form.is_valid():
            temp= form.cleaned_data['question_text']
            if temp:
                q= Question(question_text=temp, pub_date=timezone.now())
                q.save()
                return render(request, 'polls/ok.html', {'pre_link': '/polls'})
            else:
                return render(request, 'polls/error.html', {'pre_link': '/polls'})
    else:
        form= AddQuestionForm()

    return render(request, 'polls/question_add.html', {'form': form})

def result(request):
    questions= Question.objects.all()
    choices= Choice.objects.order_by('-votes')
    context={
        'questions': questions,
        'choices': choices,
    }
    template= loader.get_template('polls/question_result.html')
    return HttpResponse(template.render(context, request))


def vote(request, question_id):
    question_obj= get_object_or_404(Question, id=question_id)
    choices= Choice.objects.filter(question_id=question_id)
    template= loader.get_template('polls/question_vote.html')

    if request.method=='POST':
        add_form= AddChoiceForm(request.POST)
        vote_form= VoteForm(request.POST, question_id=question_id)
        if add_form.is_valid():
            # questionid= form.cleaned_data['question_id']
            choicetext= add_form.cleaned_data['choice_text']
            if choicetext:
                c= Choice(question=question_obj, choice_text= choicetext)
                c.save()
                return render(request, 'polls/ok.html', {'pre_link': '/polls/'+str(question_id)+'/vote'})
            else:
                return render(request, 'polls/error.html', {'pre_link': '/polls/'+str(question_id)+'/vote'})

        if vote_form.is_valid():
            choice= vote_form.cleaned_data['votes']
            if choice:
                choice.votes = choice.votes+1
                choice.save()
                return render(request, 'polls/ok.html', {'pre_link': '/polls'})
            else:
                return render(request, 'polls/error.html', {'pre_link': '/polls'})
    else:
        add_form= AddChoiceForm()
        vote_form= VoteForm(question_id=question_id)

    context={
        'question_object': question_obj,
        'choices': choices,
        'add_form' : add_form,
        'vote_form' : vote_form,
    }
    return HttpResponse(template.render(context, request))