import sys
rate_per_unit = 5

# Read units from file (for Jenkins automation)
with open("units_input.txt", "r") as file:
    units = float(file.read().strip())

# Calculate bill
total_bill = units * rate_per_unit

# Display result
print("Units Consumed:", units)
print("Rate Per Unit: ₹", rate_per_unit)
print("Total Electricity Bill: ₹", total_bill)
