from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from django.urls import reverse_lazy
from webapp.forms import SimpleSearchForm, PollForm, ChoiceForm
from webapp.models import Poll, Choice
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/choice_delete.html'

    def get_success_url(self):
        return reverse_lazy('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceUpdateView(UpdateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choice/choice_update.html'

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_view', pk=poll.pk)

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choice/choice_create.html'

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('index')
