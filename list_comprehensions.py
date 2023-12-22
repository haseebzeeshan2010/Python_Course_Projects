usernames = ['John_Kitchen', 'Paul_House Floor', 'Sarah_Management', 'Lisa_Cold Storage', 'Ryan_Inventory Mgmt', 'Gill_Cashier']

# List comprehension looks like:
# list = [ <operation> for <item> in <list> ]
username =  [item.replace(" ","_") for item in usernames]
print("List comprehension:  ",username)


employees = [{'id': 12345, 'name': 'John', 'department': 'Kitchen'}, {'id': 12456, 'name': 'Paul', 'department': 'House Floor'}, {'id': 12478, 'name': 'Sarah', 'department': 'Management'}, {'id': 12434, 'name': 'Lisa', 'department': 'Cold Storage'}, {'id': 12483, 'name': 'Ryan', 'department': 'Inventory Mgmt'}, {'id': 12419, 'name': 'Gill', 'department': 'Cashier'}]

# Dictionary comprehension looks like:
# dict = { key : value for <item> in <list> }
#or
#dict = { key:value for key, value in <sequence> if <condition> } 
employID = {employee['name'][0] : employee['id'] for employee in employees}
print("Dictionary comprehension:  ", employID)