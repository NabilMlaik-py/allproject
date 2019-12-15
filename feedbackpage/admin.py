from django.contrib import admin
from .models import *


class feedbackpersom(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback')


admin.site.register(feedbackperson, feedbackpersom)
