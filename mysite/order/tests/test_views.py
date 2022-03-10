from datetime import datetime
from django.urls import reverse


def test_create_new_order(db, client, new_type, new_product):
    """Тест создания нового заказа"""
    data = {
        'type': new_type,
        'product': new_product,
        'date': datetime.today().strftime("%Y.%d.%m"),
        'address_form-0-city': 'Город',
        'address_form-0-street': 'Улица',
        'address_form-0-house': '500',
        'address_form-0-apartment': '18'
    }
    url = reverse('order_page')
    response = client.post(path=url, data=data)
    assert response.status_code == 200