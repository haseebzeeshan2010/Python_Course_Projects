def divide_by(a,b):
    return a / b

#Example 1
try:
    ans = divide_by(40,0)
except: #just outputs custome message if error occurs
    print("Something went wrong!")

#Example 2
try:
    ans = divide_by(40,0)
except Exception as e: # e is the actual error, so in this example both the custom message and the error are output
    print("Something went wrong!", e)
    print(e.__class__) # outputs class of error

#Example 3
try:
    ans = divide_by(40,0)
except ZeroDivisionError as e: # deals with a specific type of error
    print(e, "We cannot divide by zero")

#Example 4
try:
    ans = divide_by(40,0)
except ZeroDivisionError as e: # deals with a specific type of error
    print(e, "We cannot divide by zero")
except Exception as e: # you can add multiple exceptions for a single try clause
    print(e, "Something went wrong")

#Note: The base class for exceptions in python is Exception