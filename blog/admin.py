from django.contrib import admin
from . import models

class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    extra = 0

admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Comment)
