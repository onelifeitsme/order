from django.db import models


class ProductType(models.Model):
    """Модель типа товара"""
    name = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Название товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'


class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Название товара')
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Тип товара', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    """Модель заказа"""
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, blank=False, verbose_name='Тип товара')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, verbose_name='Название товара')
    date = models.DateField('Дата доставки', auto_now=False, auto_now_add=False, blank=False)
    attachment = models.FileField(upload_to='attachments/%Y/%m/%d/', null=True, blank=True, verbose_name='Файл')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return f'{self.product.name}, {self.date}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'