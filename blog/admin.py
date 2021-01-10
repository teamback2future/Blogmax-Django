from django.contrib import admin
from . models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["author"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    class Meta:
        model = Post

