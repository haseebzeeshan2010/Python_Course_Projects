#Using the splice function

trial = "reversal" # The string to be reversed
new_trial = trial[::-1]
print(new_trial)

#Using recursion

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[:1]) + str[0]
    
str = "reversal"
reverse = string_reverse(str)
print(reverse)