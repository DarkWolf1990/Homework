from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя')
    email = models.EmailField(verbose_name='email')
    phone = models.PositiveIntegerField(null=True, blank=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    register = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата регистрации')

