import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def first_category():
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации",
                    products=[Product("Iphone 15", "512GB, Gray space", 210000.0, 8)]
                    )


@pytest.fixture
def second_category():
    return Category(name="Телевизоры",
                    description="Современный телевизор, который позволяет наслаждаться просмотром",
                    products=[Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)]
                    )


@pytest.fixture
def empty_list_product():
    return Category(name="Телевизоры",
                    description="Современный телевизор, который позволяет наслаждаться просмотром",
                    products=[]
                    )
