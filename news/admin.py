from django.contrib import admin
from .models import News, Category, Comment
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    # list_filter=["title", "description","category"]
    list_display=["title", "description","category"]

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Comment)

