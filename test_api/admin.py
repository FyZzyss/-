from django.contrib import admin
from .models import Polls, Answer, UserAnswer
# Register your models here.
admin.site.register(Polls)
admin.site.register(Answer)
admin.site.register(UserAnswer)