from shopping_data_functions import Shop_Data

shop_data = Shop_Data()
shop_data.gather_all()

print("\n\t Welcome dear customer!")
print("\nAttention! Firstly, choose where do you want to go and see what shop offers/"
      "\nCurrency for all operations: \"$\":"
      "\nIf you want to add/remove item type 'add'/'remove' before writing the ID of product. \n/"
      "or You could see the cart by typing 'report'")

customer_in = True
while customer_in:
    while True:
        part = input("\n\nChoose where to go (grocery, cakes, books): ").lower()
        if part == "grocery":
            shop_data.show_grocery_list()
            break
        elif part == "cakes":
            shop_data.show_cakes_list()
            break
        elif part == "books":
            shop_data.show_books_list()
            break
        elif part == "report":
            shop_data.report()
        elif part == "quit":
            customer_in = False
            break
        else:
            continue

    if part == "quit":
        break

    while True:
        ask = input("\n\nIf you want to add/remove item type 'add'/'remove': ").lower()
        if ask == "quit":
            break
        elif ask == "report":
            shop_data.report()
        elif ask == "add":
            while True:
                item = input("\n\nType the ID of product: ")
                if item == "quit":
                    break
                try:
                    amount = float(input("Type amount of item: "))
                except:
                    print("You have not typed digits only")
                    continue
                if amount > 0 and shop_data.isin(item):
                    shop_data.add_item(item, amount)
                else:
                    print("\nInvalid type. Try again.")
        elif ask == "remove":
            while True:
                item = input("\n\nType the ID of product: ").lower()
                if item == "quit":
                    break
                try:
                    amount = float(input("Type amount of item: "))
                except:
                    print("You have not typed digits only")
                    continue
                if amount > 0 and shop_data.isin(item):
                    shop_data.remove_item(item, amount)
                    break
                else:
                    print("\nInvalid type. Try again.")

shop_data.report()
shop_data.calculate_bill()


# orders = {}
# n = 1
# while True:
#     while True:
#         meal = input(f"Type {n}-order (or Type quit): ").lower()
#         if meal not in menu and meal != "quit":
#             print(f"We do not have {meal} meal\nPlease, select other type\n")
#             continue
#         else:
#             break
#     if meal == "quit":
#         break
#     if meal in orders:
#         orders[meal]["frequency"] += 1
#         n += 1
#     elif meal in menu:
#         print(f"{meal}: {menu[meal]}$")
#         orders.update({meal: {"price": menu[meal], "frequency": 1}})
#         n += 1
#     else:
#         print(f"Sorry, we have not {meal}")
#
# print("\nHere your orders below:")
# for b in orders.keys():
#     print(f"{b}: {orders[b]['price']}$\n"
#           f"Number of orders: {orders[b]['frequency']}")
#     orders[b]["price"] *= orders[b]['frequency']
# total = 0
# for n in orders:
#     total += orders[n]["price"]
# print(f"\nTotal bill: {total}$")
#
# print(orders)
