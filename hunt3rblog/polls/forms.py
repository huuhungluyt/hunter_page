from django import forms

from .models import Choice, Question

class AddQuestionForm(forms.Form):
    question_text=forms.CharField(label='Question content', max_length=256)


class AddChoiceForm(forms.Form):
    # question_id= forms.IntegerField(required=False, widget=forms.HiddenInput())
    choice_text=forms.CharField(label='Choice content', max_length=256)


class VoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id')
        question_obj= Question.objects.get(id=question_id)
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['votes'] = forms.ModelChoiceField(queryset=Choice.objects.filter(question=question_obj), widget=forms.RadioSelect(), empty_label=None)