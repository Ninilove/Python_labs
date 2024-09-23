# Write a program that will display the account ID  from the arn below: Display on the screen the account ID is account_id

# The ID number is the 5th part of this arn, therefore we will use the split function to extract the ID number

arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"

# Here we are using index 4 because in Python, lists are 0-indexed

account_id = arn.split(':')[4]


print(f"The account ID is: {account_id} ")