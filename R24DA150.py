import json

inventory_file = "inventory.json"
supplier_file = "suppliers.json"

def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

class Inventory:
    def add_product(self):
        data = load_data(inventory_file)
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))

        data[pid] = {
            "name": name,
            "quantity": qty,
            "price": price
        }

        save_data(inventory_file, data)
        print("Product Added!\n")

    def update_stock(self):
        data = load_data(inventory_file)
        pid = input("Enter Product ID to update: ")

        if pid in data:
            qty = int(input("Enter new quantity: "))
            data[pid]["quantity"] = qty
            save_data(inventory_file, data)
            print("Stock Updated!\n")
        else:
            print("Product not found!\n")

    def record_sale(self):
        data = load_data(inventory_file)
        pid = input("Enter Product ID sold: ")

        if pid in data:
            qty = int(input("Enter quantity sold: "))

            if data[pid]["quantity"] >= qty:
                data[pid]["quantity"] -= qty
                save_data(inventory_file, data)
                print("Sale Recorded!\n")
            else:
                print("Not enough stock!\n")
        else:
            print("Product not found!\n")

    def stock_report(self):
        data = load_data(inventory_file)
        print("\nSTOCK REPORT")
        for pid, details in data.items():
            print(pid, details)
        print()

    def low_stock(self):
        data = load_data(inventory_file)
        print("\nLOW STOCK PRODUCTS")
        for pid, details in data.items():
            if details["quantity"] < 5:
                print(details["name"], details["quantity"])
        print()

class Supplier:
    def add_supplier(self):
        data = load_data(supplier_file)
        sid = input("Enter Supplier ID: ")
        name = input("Enter Supplier Name: ")
        phone = input("Enter Phone: ")

        data[sid] = {
            "name": name,
            "phone": phone
        }

        save_data(supplier_file, data)
        print("Supplier Added!\n")

def menu():
    inv = Inventory()
    sup = Supplier()

    while True:
        print("====== INVENTORY MANAGEMENT SYSTEM ======")
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Record Sale")
        print("4. Stock Report")
        print("5. Low Stock Check")
        print("6. Add Supplier")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            inv.add_product()
        elif choice == '2':
            inv.update_stock()
        elif choice == '3':
            inv.record_sale()
        elif choice == '4':
            inv.stock_report()
        elif choice == '5':
            inv.low_stock()
        elif choice == '6':
            sup.add_supplier()
        elif choice == '7':
            break
        else:
            print("Invalid choice!\n")

menu()