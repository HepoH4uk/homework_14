class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, prod_data):
        return cls(name=prod_data.get("name"),
                   description=prod_data.get("description"),
                   price=prod_data.get("price"),
                   quantity=prod_data.get("quantity"))
