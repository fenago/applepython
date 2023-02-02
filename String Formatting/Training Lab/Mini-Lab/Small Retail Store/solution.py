#Small Retail Store
#Small Retail Store
def generate_receipt(items):
    print("===== Dr lee Retail Store =====")
    print("Receipt:")
    total = 0
    for item in items:
        print(f"{item[0]} x {item[1]} = {item[2] * item[1]:.2f}")
        total += item[2] * item[1]
    print("=============================")
    print(f"Total: {total:.2f}")
    print("Thanks for shopping with us!")

if __name__ == "__main__":
    items = [("Item 1", 2, 5.0), ("Item 2", 3, 2.5), ("Item 3", 1, 10.0)]
    generate_receipt(items)
