from flask import Flask

balance = 10000
access = True

def mainMenu():
    global balance
    global access

    def lockout_func():
        global access
        if access == False :
            print(" ")
            print("!!!!!!!!!!")
            print(" ")
            print("You're account has been frozen.  Please contact customer support for your unlock pin!")
            print(" ")
            print("!!!!!!!!!!")
            print(" ")
            lockout_input = int(input("Please enter unlock pin -> "))
            if lockout_input == 3201:
                    access = True
                    print(" ")
                    anykey=input("Pin accepted! Press enter to return to the menu")
                    print(" ")
                    mainMenu()
                     
            else:
                print("That is not a valid input, please enter a valid unlock pin")
                lockout_func()
               
    print(" ")
    print("Hello, welcome to your virtual wallet!")
    print(" ")
    print("Please choose one of the following options:")
    print(" ")
    print("1. Check balance")
    print(" ")
    print("2. Withdraw")
    print(" ")
    print("3. Deposit")
    print(" ")
    print("4. Exit the program")
    print(" ")

    original_input = int(input("Please enter a number -> "))

    if original_input == 1203:
        access = False
        lockout_func()

    elif original_input == 1:
        print(" ")
        print(f"You're current balance is ${balance}")
        print(" ")
        anykey=input("Press enter to return to the Main Menu")
        mainMenu()

    elif original_input == 2:
        print(" ")
        withdraw_amount = int(input("How much would you like to withdraw?  $"))
        end_amount_withdraw = balance - withdraw_amount
        balance = end_amount_withdraw
        print(" ")
        print(f"Withdrawl complete.  Your current balance is ${end_amount_withdraw}")
        print(" ")
        anykey=input("Press enter to return to the Main Menu")
        mainMenu()
        
    elif original_input == 3:
        print(" ")
        deposit_amount = int(input("How much would you like to deposit?  $"))
        end_amount_deposit = balance + deposit_amount
        balance = end_amount_deposit
        print(" ")
        print(f"Deposit complete.  Your current balance is ${end_amount_deposit}")
        print(" ")
        anykey=input("Press enter to return to the Main Menu")
        mainMenu()
        
    elif original_input == 4:
        exit

    else:
        print(f"{original_input} is not a valid input.  Please enter a number between 1 - 4")
        anykey=input("Press enter to return to the Main Menu")
        mainMenu()

mainMenu()