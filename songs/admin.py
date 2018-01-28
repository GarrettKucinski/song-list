from django.contrib import admin
from .models import Performer, Song


class SongInline(admin.StackedInline):
    model = Song


class PerformerAdmin(admin.ModelAdmin):
    inlines = [SongInline, ]


admin.site.register(Performer, PerformerAdmin)
admin.site.register(Song)
