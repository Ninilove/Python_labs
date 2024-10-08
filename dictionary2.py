# print out the last name of the second employee. Please search through the dictionary below: ** Alexandra

d = {"employees":[{"firstName": "John", "LastName":"Doe"},
{"firstName": "Anna", "lastName": "Smith"},
{"firstName": "Peter", "lasName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
{"firstName":"Jessy", "lastName": "Petter"}]}

# using the index method to find the last name of the second employee  
# also, using the get method to look for Amanda, and in case it's not on the dictionary it will output a none message

print(d["employees"][1]["lastName"])
print(d.get("Amanda"))