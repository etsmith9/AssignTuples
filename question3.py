# Task 1: Customer Order Processing Refine your skills in tuple unpacking by 
# managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's 
# order. Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.

# - Write a function to iterate over the list of orders. 
# - Unpack each tuple in the list and format the details for display.

def display_orders(orders):
    for order in orders:
        print(f"Name: {order[0]}, Product Ordered: {order[1]}, Quantity Ordered: {order[2]}")

def main():
    orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Emily", "Calculator", 1),
    ("Harry", "Camera", 3)
]
    
    while True:
        print("\nWelcome to your order management system")
        print("\n1. Display Orders")
        print("2. Exit")
        choice = input("Enter your choice:  ")

        if choice == "1":
            display_orders(orders)
        elif choice == "2":
           print("Exiting program")
           break
        else:
           print("Invalid choice, please try again.")


if __name__ == '__main__':
   main()