from django.contrib import admin

# Register your models here.
from .models import Statements,Sessions,Questionnaire

admin.site.register(Statements)
admin.site.register(Sessions)
admin.site.register(Questionnaire)