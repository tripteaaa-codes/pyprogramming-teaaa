# Electricity Bill Management System

import pandas as pd

# Function to calculate electricity bill
def calculate_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

    return bill

# Function to add customer details
def add_customer():
    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")
    previous_reading = int(input("Enter Previous Meter Reading: "))
    current_reading = int(input("Enter Current Meter Reading: "))

    # Calculate unit consumption
    units = current_reading - previous_reading

    # Calculate bill amount
    bill_amount = calculate_bill(units)

    # Store data in dictionary
    customer_data = {
        "Customer ID": customer_id,
        "Customer Name": customer_name,
        "Previous Reading": previous_reading,
        "Current Reading": current_reading,
        "Units Consumed": units,
        "Bill Amount": bill_amount
    }

    return customer_data

# Main Program
print("=== Electricity Bill Management System ===")

customer = add_customer()

# Create DataFrame
df = pd.DataFrame([customer])

# Display Bill
print("\n--- Electricity Bill ---")
print(df)

# Save billing history to CSV file
df.to_csv("billing_history.csv", mode='a', index=False, header=False)

print("\nBilling history saved successfully.")
