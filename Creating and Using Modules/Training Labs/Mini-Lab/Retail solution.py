
import csv

def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

if __name__ == '__main__':
    file_path = r'C:\Users\Dr Shafiq Ur Rehman\sales_data1.csv'
    data = read_data(file_path)
   
    
def process_data(data):
    product_count = {}
    for row in data:
        product = row[0]
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1
    return product_count
def find_popular(product_count):
    popular = []
    max_count = 0
    for product, count in product_count.items():
        if count > max_count:
            popular = [product]
            max_count = count
        elif count == max_count:
            popular.append(product)
    return popular
if __name__ == '__main__':
    file_name = 'sales_data1.csv'
    data = read_data(file_name)
    product_count = process_data(data)
    popular = find_popular(product_count)
    print('The most popular products are:')
    for product in popular:
        print(product)

