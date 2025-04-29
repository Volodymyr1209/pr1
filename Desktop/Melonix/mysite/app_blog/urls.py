from django.urls import path
from .views import HomePageView, ArticleList, ArticleDetailView, ArticlesByCategory
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', ArticleList.as_view(), name='articles-list'),
    path('articles/category/<slug:slug>/', ArticlesByCategory.as_view(), name='category-detail'),  # ← тут ОК
    path('articles/<int:year>/<int:month>/<int:day>/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


