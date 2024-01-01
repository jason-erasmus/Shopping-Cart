DONE = False   # 'constant' variable to avoid breaking while loop
basket_items = []   # empty list to store data
basket_cost = []    # empty list to store basket value
TOTAL = 0

print("\nWelcome to Food and Stuffs!")

while not DONE:    # while loop to display UI and options
    print("\n")
    print("=" * 80)
    print("This is your shopping cart: ")
    for index, basket in enumerate(basket_items):
        cost = round(basket_cost[index], 2)
        print(f"{index+1}.{basket.capitalize()}  |  £{cost}")
    print("=" * 80)
    print("What would you like to do? ")
    print("1. Add an item to your shopping cart")
    print("2. Remove an item from your shopping cart")
    print("3. View total value of your shopping cart")
    print("4. Check out your shopping cart")
    print(" ")
    choice = input("Enter a number for the option you want to display: \n")

    if choice == "1":
        item_input = input("What would you like to add? ").lower()
        basket_items.append(item_input)
        cost_input = float(input("How much does it cost? "))
        basket_cost.append(cost_input)
        print(f"\n{item_input} has been successfully added")

    elif choice == "2": 
        item_remove = input("What would you like to remove? ").lower()
        if item_remove in basket_items:
            item_index = basket_items.index(item_remove)
            basket_items.remove(item_remove)
            basket_cost.pop(item_index)

            print(f"\n{item_remove} has succesfully been removed")
            
    elif choice == "3":
        for n in basket_cost:
            TOTAL += n
        print(" ")
        print("=" * 80)
        print(f"Your basket total is £{round(TOTAL,2)}")
        print("=" * 80)

    elif choice == "4":
        print("="*80)
        print("Thank you for shopping at Food & Stuffs!")
        DONE = True

    else:
        print("Please enter a valid option.")
