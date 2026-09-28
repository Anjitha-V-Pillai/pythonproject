class Account:

    def __init__(self):
        self.acctnumber = int(input("Enter Account number: "))
        self.acctname = input("Enter Account name: ")
        self.balance = float(input("Enter balance: "))

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance = self.balance + amount
        print("Deposit successful")

    def showbalance(self):
        print("Account number:", self.acctnumber)
        print("Account name:", self.acctname)
        print("Balance:", self.balance)


l = []

while(1):

    print("\n1. Create an account")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Show balance")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        a = Account()
        l.append(a)
        print("Account created successfully")

    elif ch == 2:
        number = int(input("Enter Account number: "))

        for i in l:
            if i.acctnumber == number:
                i.withdraw()
                break
        else:
            print("Account Does not exist")

    elif ch == 3:
        number = int(input("Enter Account number: "))

        for i in l:
            if i.acctnumber == number:
                i.deposit()
                break
        else:
            print("Account Does not exist")

    elif ch == 4:
        number = int(input("Enter Account number: "))

        for i in l:
            if i.acctnumber == number:
                i.showbalance()
                break
        else:
            print("Account Does not exist")

    elif ch == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")