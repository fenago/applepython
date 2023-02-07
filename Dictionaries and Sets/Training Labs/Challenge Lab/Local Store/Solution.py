import csv

class Product:
    def __init__(self, name, price, product_code, category):
        self.name = name
        self.price = price
        self.product_code = product_code
        self.category = category
def read_products_from_csv(file_path):
    products = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                name, price, product_code, category = row
                price = float(price)
            except ValueError:
               
                continue
            products.append(Product(name, price, product_code, category))
    return products

def create_product_dict(products):
    product_dict = {}
    for product in products:
        product_dict[product.product_code] = product
    return product_dict

def get_product_by_code(product_dict, product_code):
    return product_dict.get(product_code)

def get_products_by_category(product_dict, category):
    return set([product for product in product_dict.values() if product.category == category])

def get_category_counts(product_dict):
    category_counts = {}
    for product in product_dict.values():
        if product.category in category_counts:
            category_counts[product.category] += 1
        else:
            category_counts[product.category] = 1
    return category_counts

def main():
    file_path = "inventory.csv"
    products = read_products_from_csv(file_path)
    product_dict = create_product_dict(products)

    product_code = "P001"
    product = get_product_by_code(product_dict, product_code)
    if product:
        print(f"Product with code {product_code}: {product.name}")
    else:
        print(f"No product found with code {product_code}")

    category = "Electronics"
    products_in_category = get_products_by_category(product_dict, category)
   

    category_counts = get_category_counts(product_dict)
    print("Category counts:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

if __name__ == "__main__":
    main()
