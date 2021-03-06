from django.contrib import admin
from webapp.models import Choice, Poll, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'date')
    search_fields = ('question',)
    list_filter = ('date',)


admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Poll, PollAdmin)
