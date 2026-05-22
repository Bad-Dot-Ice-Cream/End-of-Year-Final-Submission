# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("How much was the total bill?\n>  $"))

tip = int(input("What percent tip would you like to give?\n(typically range from 10, 12, 15, or 20 depending on quality of service)?\n>  "))

bill_split = int(input("How many people are splitting the bill?\n>  "))
tip_as_percent = tip / 100

total_tip = round(bill * tip_as_percent, 2)
total_bill = round(bill + total_tip, 2)
bill_per_person = total_bill / bill_split

final_amount = round(bill_per_person, 2)
print("-----------------------")
print(f"Your total default tip is ${total_tip}")
print(f"Your bill in total is ${total_bill}")
print(f"In total, each person in your party should pay ${final_amount}")
print("-----------------------")