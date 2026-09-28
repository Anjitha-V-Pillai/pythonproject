class MyException(Exception):
    pass

try:
    n=int(input("enter the age:"))
    if (n<18):
        raise MyException("not eligible for voting")
    else:
        print("eligible for voting")
except MyException as e:
    print(e)

# ask the user to enter a number.if the number is less than or equal to 0
# raise a ValueError with the message "Number must be positive"
try:
    n=int(input("enter a number:"))
    if (n<=0):
        raise ValueError("Number must be positive")
    else:
        print("number is positive")
except ValueError as e:
    print(e)


#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")
class InvalidPasswordError(Exception):
    pass
try:
    n=(input("enter a password:"))
    if (len(n)<8):
        raise InvalidPasswordError("password must be at least 8 characters")
    else:
        print(n)
except InvalidPasswordError as e:
    print(e)
#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

class InsuffientBalanceError(Exception):
    pass
try:
    n=int(input("enter the amount:"))
    balance=5000
    if(n>balance):
        raise InsuffientBalanceError("Not Enough Balance.Transaction Failed")
    else:
        print(n)
except InsuffientBalanceError as e:
    print(e)