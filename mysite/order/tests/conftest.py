import pytest
from ..models import ProductType, Product


@pytest.fixture
def new_type(db) -> ProductType:
    """Фикстура создания типа продукта"""
    return ProductType.objects.create(name='Тип товара номер 1')


@pytest.fixture
def new_product(db, new_type) -> Product:
    """Фикстура создания товара"""
    return Product.objects.create(type=new_type, name='Название товара номер 1')
