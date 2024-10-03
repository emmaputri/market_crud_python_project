# Create a program that only uses input and print function to make fruit purchase
kiwi_price = int(input("Kiwi Price: Rp. "))
lychee_price = int(input("Lychee Price: Rp. "))
mango_price = int(input("Mango Price: Rp. "))

# The use will then be asked to enter the amount to be purchased for each fruit
kiwi_amount = int(input("Kiwi amount (unit): "))
lychee_amount = int(input("Lychee amount (unit): "))
mango_amount = int(input("Mango amount (unit): "))

# After entering the third quantity, the program will calculate the total price using the print function.
total_price_kiwi = kiwi_amount * kiwi_price
total_price_lychee = lychee_amount * lychee_price
total_price_mango = mango_amount * mango_price

# The way to calculate it is to multiply the unit price by the desired quantity of each fruit, after which the total of the three is added up to become the final price.
total_price = total_price_kiwi + total_price_lychee + total_price_mango
print("Total Price: Rp. ", total_price)

