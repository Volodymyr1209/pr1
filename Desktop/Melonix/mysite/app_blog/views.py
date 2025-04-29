from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Article
from django.views.generic import DateDetailView
from .models import Article
from django.db import models
from django.views.generic import ListView
from .models import Article, Category 

# Функціональне представлення
def home(request):
    return HttpResponse("Привіт! Це головна сторінка додатку app_blog.")

# Класове представлення
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'app_blog/index.html')



class ArticleList(ListView):
    model = Article
    template_name = 'app_blog/articles_list.html' 
    context_object_name = 'articles'



class ArticleDetailView(DateDetailView):
    model = Article
    template_name = 'app_blog/article_detail.html'
    context_object_name = 'item'
    date_field = 'pub_date'
    month_format = '%m'
    allow_future = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context





class ArticlesByCategory(ListView):
    model = Article
    template_name = 'app_blog/articles_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context
    

from django.views.generic import ListView
from .models import Article, Category

class CategoryDetailView(ListView):
    model = Article
    template_name = 'app_blog/articles_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        return Article.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


# class Article(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     pub_date = models.DateField()
#     slug = models.SlugField(unique=True)
#     main_page = models.BooleanField(default=False)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return f"/articles/{self.pub_date.year}/{self.pub_date.month:02}/{self.pub_date.day:02}/{self.slug}/"
