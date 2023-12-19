# NOTE: Kwargs are practically Args but instead you also handle keys as well as arguments

def sum_of(**kwargs):  # 2 stars make a kwarg
    sum = 0
    for k , v in kwargs.items(): # iterate through the values
        sum += v
    return sum

print(sum_of(coffee = 2.90, cake = 4.55, juice = 2.99))