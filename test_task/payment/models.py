from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Имя продукта',
    )
    description = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Описание продукта',
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-price']

    def __str__(self):
        return self.name
