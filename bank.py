# Weekly Task 02
# Craeta two variable for the input values and convert input from string to interger

amount1 = int(input('Enter amount1 (in cent): '))
amount2 = int(input('Enter amount2 (in cent):  '))

# sum both amounts and divide them via 100 to get Euro Units
total =(amount1 + amount2)/ 100

# Print out the totla with € sign in front of the number and 2 decimal places
print(f'The sum of these in € {total:.2f}')



