stock_lychee = 10
stock_mango = 10
stock_kiwi = 10

kiwi_price = int(input("Kiwi Price: Rp. "))
lychee_price = int(input("Lychee Price: Rp. "))
mango_price = int(input("Mango Price: Rp. "))

while True:
    kiwi_amount = int(input("Kiwi amount (unit): "))
    if kiwi_amount > stock_kiwi:
        print(f"There is not enough kiwi available. Available stock: {stock_kiwi}")
        print("Please input the amount again.")
    else:
        break

while True:
    lychee_amount = int(input("Lychee amount (unit): "))
    if lychee_amount > stock_lychee:
        print(f"There is not enough lychee available. Available stock: {stock_lychee}")
        print("Please input the amount again.")
    else:
        break

while True:
    mango_amount = int(input("Mango amount (unit): "))
    if mango_amount > stock_mango:
        print(f"There is not enough mango available. Available stock: {stock_mango}")
        print("Please input the amount again.")
    else:
        break

total_price_kiwi = kiwi_amount * kiwi_price
total_price_lychee = lychee_amount * lychee_price
total_price_mango = mango_amount * mango_price
total_price = total_price_kiwi + total_price_lychee + total_price_mango

print("Total Price: Rp.", total_price)

while True:
    money = int(input("Total Paid: Rp. "))
    if money < total_price:
        insufficient_payment = total_price - money  
        print("The amount of money is not enough to pay.")
        print("Insufficient payment: Rp.", insufficient_payment)
        print("Please input the amount again.")
    else:
        change = money - total_price 
        if change == 0:
            print("Thank you!")
        else:
            print("Change: Rp.", change)
        break
print("Thank you!")