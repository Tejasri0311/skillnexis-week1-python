
balance = 1000
correct_pin = "1234"


def check_balance():
    print("Your balance is Rs.", balance)


def deposit():
    global balance
    amount = float(input("Enter deposit amount: Rs. "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
        print("Updated balance: Rs.", balance)
    else:
        print("Please enter a valid amount.")


def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: Rs. "))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining balance: Rs.", balance)


def main():
    pin = input("Enter your 4-digit PIN: ")

    if pin != correct_pin:
        print("Incorrect PIN. Login failed.")
        return

    print("Login successful!")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid option. Please try again.")


main()
