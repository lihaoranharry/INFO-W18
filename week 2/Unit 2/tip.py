price = float(input("Enter the price of a meal: "))
tip = price * 0.16
total = price + tip
if total <= 10:
    print("You ate less or euqal to 10 dollars")
else:
    print("You ate more than 10 dollars")

print("A 16% tip would be", tip)
print("The total including tip would be", total)
