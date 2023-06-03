from django.contrib import admin
from .models import Post, Bookmark, Folder


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "createDate"]


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


class FolderAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


admin.site.register(Post, PostAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Folder, FolderAdmin)
