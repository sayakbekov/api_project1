from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    country = models.CharField(max_length=244, verbose_name='Страна')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Кфатегория'
        verbose_name_plural = 'Категории'


class Car(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    model = models.CharField(max_length=255, verbose_name='Модель')
    year = models.IntegerField(default=0)
    obem = models.CharField(max_length=255, verbose_name='Обьем')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'