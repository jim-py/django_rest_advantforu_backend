from django.db import models


class Post(models.Model):
    short_description = models.CharField(max_length=255, verbose_name='Краткое описание')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    tags = models.CharField(max_length=255, verbose_name='Тэги')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    photo = models.ImageField(upload_to='post/', verbose_name='Превью')

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ['-date']

    def __str__(self):
        return f'{self.title}'


class Service(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    cost = models.IntegerField(verbose_name='Цена')
    color = models.CharField(max_length=30, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Portfolio(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    photo = models.ImageField(upload_to='media/portfolio/', verbose_name='Превью')

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class PhotosPortfolio(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, verbose_name='Портфолио', null=True)
    photo = models.ImageField(upload_to='photos_portfolio/', verbose_name='Фото')
    number = models.IntegerField(verbose_name='Порядковый номер')

    class Meta:
        verbose_name = 'Фото портфолио'
        verbose_name_plural = 'Фото портфолио'
        ordering = ['number']

    def __str__(self):
        return f'{self.portfolio} - фото {self.number}'
