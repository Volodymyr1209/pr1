from django.utils import timezone
from django.db import models
from django.urls import reverse

class Category(models.Model):
    category = models.CharField('Категорія', max_length=250, help_text='Максимум 250 символів')
    slug = models.SlugField('Слаг')

    class Meta:
        verbose_name = 'Категорія для публікації'
        verbose_name_plural = 'Категорії для публікацій'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=250, help_text='Максимум 250 символів')
    description = models.TextField('Опис', blank=True)
    pub_date = models.DateTimeField('Дата публікації', default=timezone.now)
    slug = models.SlugField('Слаг', unique_for_date='pub_date')
    main_page = models.BooleanField('Головна', default=False, help_text='Показувати?')
    category = models.ForeignKey(Category, related_name='news', blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Публікація'
        verbose_name_plural = 'Публікації'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = reverse('news-detail', kwargs={
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%m"),
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug,
        })
        return url

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name='Стаття', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('Фото', upload_to='photos')
    title = models.CharField('Заголовок', max_length=250, help_text='Максимум 250 символів', blank=True)

    class Meta:
        verbose_name = 'Фото для статті'
        verbose_name_plural = 'Фото для статті'

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return self.image.name.rsplit('/', 1)[-1]




