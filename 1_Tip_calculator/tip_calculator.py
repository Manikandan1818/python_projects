print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 - "))
split = int(input("How many people to split the bill? "))

# Calculation
bill_with_tip = (tip / 100 * bill) + bill
bill_per_person = bill_with_tip / split
final_amount = round(bill_per_person, 2)

# f-string {}
print(f"Each person should pay: {final_amount}")
