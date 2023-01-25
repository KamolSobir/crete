from django.contrib import admin
from .models import Post, Comment, PhotoCreate


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author']
    search_fields = ['title', 'content', 'author']
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


# @admin.register(Follow)
# class FollowAdmin(admin.ModelAdmin):
#     pass


@admin.register(PhotoCreate)
class PhotoCreateAdmin(admin.ModelAdmin):
    pass
