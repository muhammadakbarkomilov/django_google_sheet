from django.contrib import admin
from .models import exelUser
# Register your models here.

@admin.register(exelUser)
class exelUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'phone')
    search_fields = ('name', 'email')
    list_filter = ('age',)
    ordering = ('-id',)