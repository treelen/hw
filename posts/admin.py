from django.contrib import admin

from posts.models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "category", "status"]
    list_filter = ["status", "category"]
    list_editable = ["status", "category"]