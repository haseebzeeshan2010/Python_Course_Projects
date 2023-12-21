menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]
def find_coffee(coffee):
    if coffee[0] == 'c': # Find the values which start with 'c'
        return coffee


#Maps take 2 arguments:
#map(function,arguments for the function)
#NOTE: The map function passes inputs into the function one-by-one so no iteration of a for loop is required
        
map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)


#------------------Filter-------------------#


filter_coffee = filter(find_coffee,menu)
print(filter_coffee)
for x in map_coffee:
    print(x)


#difference between map and filter:
    
#map takes in all objects of a list and applies a function
#filter does the same,but takes the results and creates a list with only the true values