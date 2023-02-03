deliveries = [
    {
        'weight': 10,
        'destination': 'New York',
        'status': 'delivered',
        'delivery_date': '2022-01-01'
    },
    {
        'weight': 20,
        'destination': 'London',
        'status': 'in transit',
        'delivery_date': '2022-02-01'
    },
    {
        'weight': 15,
        'destination': 'Paris',
        'status': 'delivered',
        'delivery_date': '2022-03-01'
    }
]

# sort the deliveries by delivery date
deliveries.sort(key=lambda x: x['delivery_date'])

# display the deliveries
for delivery in deliveries:
    print(f"Weight: {delivery['weight']} Destination: {delivery['destination']} Status: {delivery['status']} Delivery Date: {delivery['delivery_date']}")
