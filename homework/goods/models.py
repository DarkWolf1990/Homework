from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    count = models.IntegerField(verbose_name='Количество')
    upload = models.ImageField(upload_to='static/upload/% Y/% m/% d/')
    add_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления товара')
