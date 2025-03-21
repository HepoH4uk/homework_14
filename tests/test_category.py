from src.product import Product
from src.product import Smartphone
from src.product import LawnGrass
import pytest


def test_category_1(first_category):
    first_category.category_count = 1
    product = []
    product.append(first_category.products)
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(product) == 1


def test_category_2(first_category, second_category):
    assert first_category.category_count == 3
    assert second_category.product_count == 3
    assert first_category.product_count == 3


def test_empty_list_product(empty_list_product):
    assert empty_list_product.category_count == 4
    assert empty_list_product.product_count == 3


def test_products_list(first_category, second_category):
    # assert first_category.products == 'Смартфоны, количество продуктов: 5'
    # assert second_category.products == 'Телевизоры, количество продуктов: 7'
    print(first_category.products)
    print(second_category.products)


def test_add_new_product(first_category):
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    first_category.add_product(product)
    assert first_category.products == ('Iphone 15, 210000.0 руб., Остаток: 8 шт.\n'
                                       'Xiaomi Redmi Note 11, 31000.0 руб., Остаток: 14 шт.')


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 8"


def test_add_new_product_2(first_smartphone):
    product = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    first_smartphone.add_product(product)
    assert first_smartphone.products == ('Iphone 15, 210000.0 руб., Остаток: 8 шт.\n')


def test_wrong_product_2(first_smartphone):
    product = "Wrong product"
    first_smartphone.add_product(product)
    with pytest.raises(TypeError):
        result = first_smartphone + 1