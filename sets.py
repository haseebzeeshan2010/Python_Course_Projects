# NOTE: Sets do not take duplicate values
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

print(set_a.add(6)) # add a value

print(set_a.remove(6)) # removes a specified value (using discard instead of remove does the same thing)

print(set_a.union(set_b)) # joins the two sets, minus the duplicate values

# The same thing as union can be achieved by doing:
#print(set_a | set_b)

print(set_a.symmetric_difference(set_b)) # displays elements in set a or b, but not ones that occur in both 
#Can also be done like this: print(set_a ^ set_b)