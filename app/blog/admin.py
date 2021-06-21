from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ["author", "title", "post_body", "ts_posted", "ts_changed"]
    readonly_fields = ["ts_posted", "ts_changed"]
