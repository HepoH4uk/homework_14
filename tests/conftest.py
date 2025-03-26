import pytest

from src.category import Category
from src.product import Product, LawnGrass, Smartphone


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
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


@pytest.fixture
def first_smartphone():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )


@pytest.fixture
def second_smartphone():
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space"
    )


@pytest.fixture
def first_grass():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )


@pytest.fixture
def second_grass():
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый"
    )


@pytest.fixture
def product_zero_quantity():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=0,
    )


@pytest.fixture
def zero_price_category():
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации",
                    products=[Product("Iphone 15", "512GB, Gray space", 0, 8)]
                    )


@pytest.fixture
def zero_products_category():
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации",
                    products=None)
