from django.contrib import admin
from .models import *
from .schemas import *

# Register your models here.
admin.site.register(Alunos)
admin.site.register(AulasConcluidas)



