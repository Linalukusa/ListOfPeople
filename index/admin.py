from django.contrib import admin
from .models import People


class PostAdmin(admin.ModelAdmin):
    list_display  = ('name', )
    list_filter   = ('name',)
    search_fields = ['name', ]

admin.site.register(People )
