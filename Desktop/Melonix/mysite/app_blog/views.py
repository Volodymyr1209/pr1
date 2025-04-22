from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Функціональне представлення
def home(request):
    return HttpResponse("Привіт! Це головна сторінка додатку app_blog.")

# Класове представлення
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'app_blog/index.html')


