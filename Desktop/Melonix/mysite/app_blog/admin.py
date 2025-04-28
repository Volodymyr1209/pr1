from django.contrib import admin
from .models import Article, ArticleImage, Category

admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(Category)
