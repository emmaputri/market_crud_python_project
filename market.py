print("Welcome to Fruit Market".center(50))
print("List Menu:")
print(" 1. Showing list of fruit")
print(" 2. Add fruit")
print(" 3. Delete fruit")
print(" 4. Buy fruit")
print(" 5. Exit")

market = {
    "fruit_name": ["kiwi", "lychee", "mango", "orange"],
    "stock": {"kiwi": 29, "lychee": 37, "mango": 40, "orange": 35},
    "price_@unit": {"kiwi": 4500, "lychee": 3200, "mango": 2700, "orange": 1300},
}

while True:
    x = int(input("Enter your choice: "))

    if x not in range(1, 6):
        print("Invalid input")
        continue

    if x == 1:
        print("List of Fruit:")
        print(f"| {'Index':<10} | {'Fruit Name':<15} | {'Stock':<10} | {'Price @ Unit':<15} |") #jaraknya
        print("-" * 58) # membuat garis
        index = 0 #dari 0
        for fruit in market['fruit_name']: # membuat index
            print(f"| {index:<10} | {fruit:<15} | {market['stock'][fruit]:<10} | {market['price_@unit'][fruit]:<15} |")
            index += 1 #ditambah indexnya

    elif x == 2: #nambah buah
        add_fruit = input("Add fruit name: ")
        add_stock = int(input("Add stock: "))
        add_price = int(input("Add price: "))
        market['fruit_name'].append(add_fruit) #masukin buah ke dictionary
        market['stock'][add_fruit] = add_stock # stock yg baru dimasukin dictionary
        market['price_@unit'][add_fruit] = add_price # harga buah yg baru dimasukin dictionary
        print("Fruit added successfully!")

    elif x == 3:
        delete_index = int(input("Enter the index of the fruit to delete: "))
        if 0 <= delete_index < len(market['fruit_name']):# make sure index yg didelete tidak lebih dr index yg tersedia
            deleted_fruit = market['fruit_name'][delete_index] #
            del market['fruit_name'][delete_index]
            del market['stock'][deleted_fruit]
            del market['price_@unit'][deleted_fruit]
            print(f"{deleted_fruit} deleted successfully!")
        else:
            print("Invalid index!")
    elif x == 4:
        total_price = 0
        cart = {}  # Create an empty cart to store purchased items
        while True:
            index_fruit = int(input("Input index for fruit that you want to buy: "))
            if 0 <= index_fruit < len(market['fruit_name']):
                index_amount = int(input("How much fruit to buy (unit): "))
                fruit_name = market['fruit_name'][index_fruit]
                if index_amount > market['stock'][fruit_name]:
                    print(f"There is not enough fruit available. Available stock: {market['stock'][fruit_name]}")
                    print("Please input the amount again.")
                else:
                    market['stock'][fruit_name] -= index_amount #pengurangan stock
                    price = market['price_@unit'][fruit_name] * index_amount #harga jumlah buah yang dibeli
                    total_price += price #ditotal

                    if fruit_name in cart: #dimasukin keranjang
                        cart[fruit_name] += index_amount
                    else:
                        cart[fruit_name] = index_amount

                    buy_more = input("Do you want to buy more fruit? (yes/no): ").strip().lower()
                    if buy_more != 'yes':
                        break
            else:
                print("Invalid index! Please try again.")

        # Print the final cart summary
        print("\nFinal Cart Summary:")
        print(f"| {'Fruit Name':<15} | {'Quantity Bought':<15} | {'Remaining Stock':<15} |")
        print("-" * 50)
        for fruit, quantity in cart.items():
            print(f"| {fruit:<15} | {quantity:<15} | {market['stock'][fruit]:<15} |")

        print(f"\nTotal amount to pay: Rp. {total_price}")

        # Payment process
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

    elif x == 5:
        print("Thank You!")
        break