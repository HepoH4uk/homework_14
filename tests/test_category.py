
def test_category_1(first_category):
    first_category.category_count = 1
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.products) == 1


def test_category_2(first_category, second_category):
    assert first_category.category_count == 2
    assert second_category.product_count == 2
    assert first_category.product_count == 2


def test_empty_list_product(empty_list_product):
    assert empty_list_product.category_count == 1
    assert empty_list_product.product_count == 0
