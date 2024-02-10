print("WELCOME")
x = float(input("Insert the money "))

while True:

    print("1. COKE")
    print("2. JUICE")
    print("3. MINERAL WATER")
    print("4. ICED COFFEE")
    print("5. ICE TEA")

    operation = input("Select the operation you want to perform: ")

    if operation == '1':
        if x >= 3:
            print("Coke is being dispensed")
            x -= 3
            print("Change:", x)
        else:
            print("Sorry, you don't have enough money for Coke.")

    elif operation == '2':
        if x >= 2:
            print("Juice is being dispensed")
            x -= 2
            print("Change:", x)
        else:
            print("Sorry, you don't have enough money for Juice.")

    elif operation == '3':
        if x >= 1.5:
            print("Mineral water is being dispensed")
            x -= 1.5
            print("Change:", x)
        else:
            print("Sorry, you don't have enough money for Mineral Water.")

    elif operation == '4':
        if x >= 1.5:
            print("Iced coffee is being dispensed")
            x -= 1.5
            print("Change:", x)
        else:
            print("Sorry, you don't have enough money for Iced Coffee.")

    elif operation == '5':
        if x >= 1.5:
            print("Ice tea is being dispensed")
            x -= 1.5
            print("Change:", x)
        else:
            print("Sorry, you don't have enough money for Ice Tea.")

    elif operation == 'exit':
        print("Thank you for using our service")
        print("change:", x)
        break

    elif not operation.isdigit() or int(operation) > 5:
        print("You entered an invalid number")
        print("Please enter the number again")
        print()


    decision = input("Would you like to buy another product? (yes/no): ")
    if decision.lower() != 'yes':
        print("Thank you for using our service")
        print("change:", x)
        break
