# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders:
def process_orders(orders):
    for name, product, quantity in orders:
        print(f"Customer: {name} | Product: {product} | Quantity: {quantity}")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3)
]
process_orders(orders)