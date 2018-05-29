cost = float(input("Total cost? "))
print()
money_paid = float(input("Money given? "))
print()

calc_change = money_paid - cost

print("Change:", (round(calc_change, 2)))

change = calc_change

#find dollar
dollar = 1.00
dollar_divide = int(change/dollar)
print(dollar_divide, "dollar(s)")

#calculate remainder of change after dollar calculation
a = change - dollar_divide
change_left = round(a, 2)

#find quarter
quarter = 0.25
quarter_divide = int(change_left/quarter)
print(quarter_divide, "quarter(s)")

#calculates left change after dollar and quarter values
change_left_second = (round(quarter_divide * quarter - change_left, 2)* -1)

#calculate dime
dime = 0.10
dime_divide = int(change_left_second/dime)
print(dime_divide, "dime(s)")

#calculates left change after dollar, quarter, and dime values
change_left_third = (round(dime_divide * dime - change_left_second, 2)* -1)

#calculate number of nickels
nickel = 0.05
nickel_divide = (int(change_left_third/nickel))
print(nickel_divide, "nickel(s)")

#calculate change left after dollar, quarter, dime, and nickel values
change_left_last = (round(nickel_divide * nickel - change_left_third, 2)* -1)

#calculate_number of pennies from change_left_last
penny = 0.01
penny_divide = int(change_left_last/penny)
print(penny_divide, "pennie(s)")
