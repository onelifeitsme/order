from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Название товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True, verbose_name='На')
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Тип товара', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, blank=False)
    date = models.DateField('Дата доставки', null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/%Y/%m/%d/', null=True, blank=True)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



