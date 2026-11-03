def calculate_tip(bill, percent):
    return bill * percent / 100

bill = float(input("Enter bill amount: "))
percent = float(input("Enter tip percent: "))
print(f"Tip: {calculate_tip(bill, percent)}")