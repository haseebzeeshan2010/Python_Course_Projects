def divide_by(a,b):
    return a / b

try:
    ans = divide_by(40,0)
except: #just outputs custome message if error occurs
    print("Something went wrong!")

try:
    ans = divide_by(40,0)
except Exception as e: # e is the actual error, so in this example both the custom message and the error are output
    print("Something went wrong!", e)
    print(e.__class__) # outputs class of error