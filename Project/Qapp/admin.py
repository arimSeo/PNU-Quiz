from django.contrib import admin
from .models import Question, PnuUser, Answer

admin.site.register(Question)
admin.site.register(PnuUser)
admin.site.register(Answer)