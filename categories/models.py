from django.db import models

from categories.constants import LAPTOP_TYPES, CONDITION


class Hashtag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Хэштег"
        verbose_name_plural = "Хэштеги"


class Laptop(models.Model):
    '''References'''
    hashtags = models.ManyToManyField(Hashtag)

    '''Base fields'''
    model = models.CharField(max_length=100, verbose_name="Модель ноутбука", null=True)
    image = models.ImageField(upload_to='', verbose_name="Загрузите фото", null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Добавьте описание")
    laptop_types = models.CharField(max_length=100, choices=LAPTOP_TYPES, verbose_name="Выберите тип ноутбука",
                                    null=True)
    cost = models.PositiveIntegerField(verbose_name="Укажите цену", null=True)
    release_year = models.PositiveIntegerField(verbose_name="Укажите год выпуска", null=True)
    condition = models.CharField(max_length=50, choices=CONDITION, verbose_name="Выберите состояние", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (f"Модель: {self.model}\n"
                f"Цена: {self.cost}")

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
