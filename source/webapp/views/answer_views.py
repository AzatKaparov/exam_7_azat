from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from webapp.models import Poll, Choice, Answer
from django.views.generic import View


class AnswerView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=pk)
        choices = []
        for i in Choice.objects.all():
            if i.poll.pk == poll.pk:
                choices.append(i)
            else:
                pass
        return render(request, 'answer/answer_create.html', context={
            'poll': poll,
            'choices': choices
        })

    def post(self, request, *args, **kwargs):
        choice = self.request.POST['choice']
        exact_choice = Choice.objects.get(text=choice)
        poll = Poll.objects.get(pk=exact_choice.poll.pk)
        answer = Answer.objects.create(choice=exact_choice,
                                       poll=poll)
        answer.save()
        return redirect('index')





