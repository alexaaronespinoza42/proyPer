shopping_cart = []

while True:
    print("Welcome to the Shopping Cart Program!")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    
    action = input("Please enter an action: ")

  
    if action == "1":
        item = input("What item would you like to add? ")
        shopping_cart.append(item)
        print(f"'{item}' has been added to the cart.")

    elif action == "2":
        if len(shopping_cart) == 0:
            print("The shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for item in shopping_cart:
                print(item)

    elif action == "3":
        if len(shopping_cart) == 0:
            print("The shopping cart is empty.")
        else:
            item = input("What item would you like to remove? ")
            if item in shopping_cart:
                shopping_cart.remove(item)
                print(f"'{item}' has been removed from the cart.")
            else:
                print(f"'{item}' is not in the cart.")

    elif action == "4":
        total_cost = len(shopping_cart) * 10  # Assume each item costs $10
        print(f"The total cost of the items in the cart is ${total_cost}.")

    elif action == "5":
        # Quit the program
        print("Thank you. Goodbye.")
        break

    else:
        # Invalid input
        print("Invalid input. Please try again.")