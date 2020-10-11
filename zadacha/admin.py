from django.contrib import admin
from .models import *


@admin.register(Esep)
class EsepAdmin(admin.ModelAdmin):
    list_display = ('date',)
    search_fields = ('whatsapp','email','telegram','description')

    readonly_fields = ['whatsapp','email','telegram','description','file','deadline']

admin.site.register(Questions)
# Register your models here.
