from src.product import Product


def test_category_1(first_category):
    first_category.category_count = 1
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.products) == 1


def test_category_2(first_category, second_category):
    assert first_category.category_count == 3
    assert second_category.product_count == 3
    assert first_category.product_count == 3


def test_empty_list_product(empty_list_product):
    assert empty_list_product.category_count == 4
    assert empty_list_product.product_count == 3


def test_products_list(first_category, second_category):
    assert first_category.products == ['Iphone 15,512GB, Gray space,210000.0,8']
    assert second_category.products == ['55" QLED 4K,Фоновая подсветка,123000.0,7']


def test_add_new_product(first_category):
    product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    first_category.add_product(product)
    assert first_category.products == ['Iphone 15,512GB, Gray space,210000.0,8',
                                       '55" QLED 4K,Фоновая подсветка,123000.0,7']
