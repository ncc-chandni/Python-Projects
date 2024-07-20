
menu = {'Pizza': 50, 'Pasta': 50, 'Burger':40, 'Sandwich':40, 'Coffee':25, 'Tea':20}

print("Welcome to the Restaurant")
print("Pizza: 50 \nPasta: 50 \nBurger: 40 \nSandwich: 40 \nCoffee: 25 \nTea: 20")


order_total = 0 
items = []
while True:
    item = input("Enter the name of the item you want to order\n").capitalize()
    if item in menu:
        items.append(item)
        order_total+= menu[item]
        print(f"Your order {item} has been added to your cart")
        another_order = input("Do you want to add another item? (Yes / No)\n").capitalize()
        if another_order == 'Yes':
            continue
        else:
            break
    else:
        print(f"Order item {item} is not available yet")


print(f"Total amount : Rs.{order_total}")
print(f'Your items are : {", ".join(item for item in items)}')
