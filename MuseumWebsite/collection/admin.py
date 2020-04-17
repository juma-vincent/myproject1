from django.contrib import admin
from .models import Artefact,Comment

@admin.register(Artefact)
class ArtefactAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'publish_date')
    list_filter = ('title', 'artist', 'publish_date')
    search_fields = ('title', 'artist')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('artefact','name','created') 
    list_filter = ('artefact','name','created')   