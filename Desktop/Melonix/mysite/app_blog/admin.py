# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}
    fieldsets = (
        (None, {
            'fields': ('category', 'slug'),
        }),
    )

admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        (None, {
            'fields': ('title', 'image'),
        }),
    )

class ArticleAdmin(admin.ModelAdmin): 
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    multiupload = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    
    fieldsets = (
        (None, {
            'fields': ('pub_date', 'title', 'description', 'main_page'),
        }),
        ('Фотографи', {
            'fields': ('category',),  # ← додано ключ
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    def delete_file(self, request, obj_id):
        obj = get_object_or_404(ArticleImage, pk=obj_id)
        return obj.delete()

admin.site.register(Article, ArticleAdmin)

