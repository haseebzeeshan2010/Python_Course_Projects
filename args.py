def sum(a,b):
    return a+b

print(sum(4,5)) # Can only take 2 inputs, as there are two parameters

#This is where args are used

def sum_of(*args): # One star makes an arg
    sum = 0
    for x in args: # iterate through the arguments
        sum += x
    return sum

print(sum_of(4,5,6,7))