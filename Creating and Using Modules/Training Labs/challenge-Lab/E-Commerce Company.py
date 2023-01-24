import csv

def read_data(file_path):
    """Reads in data from a CSV file and returns it as a list of dictionaries"""
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def process_data(data):
    """Calculates the total revenue and number of orders for each customer"""
    customer_data = {}
    for row in data:
        customer_id = row['customer_id']
        revenue = float(row['revenue'])
        if customer_id in customer_data:
            customer_data[customer_id]['revenue'] += revenue
            customer_data[customer_id]['orders'] += 1
        else:
            customer_data[customer_id] = {'revenue': revenue, 'orders': 1}
    return customer_data

def find_valuable_customers(customer_data, min_revenue, min_orders):
    """Finds customers with at least a certain amount of revenue and number of orders"""
    valuable_customers = []
    for customer_id, customer_info in customer_data.items():
        if customer_info['revenue'] >= min_revenue and customer_info['orders'] >= min_orders:
            valuable_customers.append(customer_id)
    return valuable_customers

def run_analysis(file_path, min_revenue, min_orders):
    data = read_data(file_path)
    customer_data = process_data(data)
    valuable_customers = find_valuable_customers(customer_data, min_revenue, min_orders)
    print('Valuable customers:')
    for customer_id in valuable_customers:
        print(customer_id)

if __name__ == '__main__':
    file_path = r'C:\Users\Dr Shafiq Ur Rehman\customers_data.csv'
    run_analysis(file_path, 1000, 5)

