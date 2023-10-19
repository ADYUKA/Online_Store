from django.db import models


class Laptop(models.Model):

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    LAPTOP_TYPES = (
        ('Офисные','Офисные'),
        ('Игровые', 'Игровые'),
        ('Ультрабуки', 'Ультрабуки')
    )

    CONDITION = (
        ('Б\У', 'Б\У'),
        ('Новый', 'Новый')
    )

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