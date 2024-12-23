
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        open(self.__file_name, 'a').close()

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return file.read()

    def add(self, *products):
        existing_entries = self.__get_existing_product_entries()
        new_entries = []

        for product in products:
            product_str = str(product)
            if product_str in existing_entries:
                print(f'Product {product.name} already in shop')
            else:
                new_entries.append(product_str)
                existing_entries.add(product_str)

        if new_entries:
            with open(self.__file_name, 'a', encoding='utf-8') as file:
                file.write('\n'.join(new_entries) + '\n')

    def __get_existing_product_entries(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return {line.strip() for line in lines if line.strip()}

if __name__ == "__main__":
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())