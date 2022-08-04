from django.contrib import admin
from .models import Data



@admin.register(Data)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'date',)