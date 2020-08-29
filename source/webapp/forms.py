from django import forms

from webapp.models import Poll


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class PollForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Poll
