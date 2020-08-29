from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Вопрос')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    def __str__(self):
        return f'{self.pk}: {self.question}'

    class Meta:
        verbose_name_plural = 'Опросы'
        verbose_name = 'Опрос'


class Choice(models.Model):
    text = models.TextField(blank=False, null=False, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', related_name='poll_choice', on_delete=models.CASCADE,
                               verbose_name='Опрос')

    def __str__(self):
        return f'{self.pk} - {self.poll}'

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
