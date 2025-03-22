import pytest

from src.product import Product


def test_products(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_price_property(first_product):
    assert first_product.price == 180000.0


def test_price_setter(capsys, first_product):
    first_product.price = -5000
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_new_product():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_product_str(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(first_product, second_product):
    assert first_product+second_product == 1334000.0


def test_smartphone(first_smartphone):
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"


def test_grass(first_grass):
    assert first_grass.name == "Газонная трава"
    assert first_grass.description == "Элитная трава для газона"
    assert first_grass.price == 500.0
    assert first_grass.quantity == 20
    assert first_grass.country == "Россия"
    assert first_grass.germination_period == "7 дней"
    assert first_grass.color == "Зеленый"


def test_smartphone_add(first_smartphone, second_smartphone):
    assert first_smartphone+second_smartphone == 2580000.0


def test_smartphone_wrong_add(first_smartphone, first_grass):
    with pytest.raises(TypeError):
        result = first_smartphone + 1


def test_grass_add(first_grass, second_grass):
    assert first_grass + second_grass == 16750.0
