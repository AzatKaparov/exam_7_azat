from django.urls import reverse
from django.db.models import Q
from django.urls import reverse_lazy
from webapp.forms import SimpleSearchForm, PollForm
from webapp.models import Poll, Choice
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


class PollIndexView(ListView):
    template_name = 'poll/poll_index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-date']
    paginate_by = 5
    queryset = Poll.objects.all()

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(question__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll
    context_object_name = 'poll'

    def get_context_data(self, *, object_list=None, **kwargs):
        poll = self.object
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['choices'] = []
        for i in Choice.objects.all():
            if i.poll.pk == poll.pk:
                context['choices'].append(i)
            else:
                pass
        return context


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll/poll_create.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/poll_delete.html'
    success_url = reverse_lazy('index')


class PollUpdateView(UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll/poll_update.html'
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})
