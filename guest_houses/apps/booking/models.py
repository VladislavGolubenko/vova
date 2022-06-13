from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    number = models.CharField(max_length=17, verbose_name='Номер телефона', null=True, blank=True)
    passport = models.CharField(max_length=15, verbose_name='Паспортные данные', null=True, blank=True)
    id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='user_profile',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профиль пользователя'


class Booking(models.Model):
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания')
    id_realty = models.ForeignKey(
        'Realty',
        on_delete=models.CASCADE,
        verbose_name='Недвижимость',
        related_name='realty',
        null=True,
        blank=True
    )
    id_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='user',
        null=True,
        blank=True
    )

    date_creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    amount = models.IntegerField(verbose_name='Цена на момент покупки')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
        ordering = ['-date_creation']


class Realty(models.Model):
    types = (
        ('Номер в гостевом доме', 'Номер в гостевом доме'),
        ('Квартира', 'Квартира'),
        ('Частный дом', 'Частный дом'),
        ('Номер в гостинице', 'Номер в гостинице')
    )

    regions = (
        ('Краснодарский край', 'Краснодарский край'),
        ('Крым', 'Крым'),
        ('Кавказ', 'Кавказ'),
        ('Центральная Россия', 'Центральная Россия'),
        ('Сибирь', 'Сибирь'),
        ('Дальний восток', 'Дальний восток'),
        ('Урал', 'Урал')
    )

    type = models.CharField(max_length=250, verbose_name='Тип', choices=types)
    rooms = models.IntegerField(verbose_name='Кол-во комнат')
    bedrooms = models.IntegerField(verbose_name='Кол-во спален')
    price = models.FloatField(verbose_name='Цена')
    region = models.CharField(max_length=250, verbose_name='Регион', choices=regions)
    address = models.CharField(max_length=150, verbose_name='Адрес')
    detail = models.CharField(max_length=5000, verbose_name='Подробности', null=True, blank=True)

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимости'


class Pictures(models.Model):

    id_realty = models.ForeignKey(
        'Realty',
        on_delete=models.CASCADE,
        verbose_name='id недвижимости',
        related_name='pictures',
        null=True,
        blank=True
    )
    image_link = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        verbose_name='Ссылка на изображение'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
