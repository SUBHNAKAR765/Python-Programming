# Sample data
data = [
    "10745032560 Sagar Kumar Tripathy 18,700",
    "10745032619 Amrit Balav Chaturbedy 93,000",
    "10745032620 Pradeep Kumar Pradhan 45,900",
    "10745032781 Joginder Jaspal Bhatti 56,700",
    "10745032543 Akash Ranjan Samal 78,800",
    "10745032321 Bismay Ranjan Biswal 85,500"
]

for line in data:
    columns = line.split()
    account_number = columns[0]
    balance = columns[-1]
    name_parts = columns[1:-1]

    # Assign name parts with default empty strings for middle name if not present
    first_name = name_parts[0]
    middle_name = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""
    last_name = name_parts[-1] if len(name_parts) > 1 else ""

    print(f"*************** Bank Balance {account_number} Statement ***************")
    print(f"Customer_Account: {account_number}")
    print(f"Customer_FName: {first_name}")
    print(f"Customer_MName: {middle_name}")
    print(f"Customer_LName: {last_name}")
    print(f"Account_Balance: {balance}")
    print("*")