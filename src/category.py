from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        product_quantity = 0
        for product in self.__products:
            product_quantity += product.quantity

        return f"{self.name}, количество продуктов: {product_quantity}"

    @property
    def products(self):
        products_info = []
        for product in self.__products:
            products_info.append(f"{product.name}, {product.price} руб., Остаток: {product.quantity} шт.")
        return '\n'.join(products_info)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1
