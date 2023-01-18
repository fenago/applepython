Mini _lab 
# Step 1: Create variables and assign values
name = "John Smith"
address = "123 Main St"
zipcode = "12345"
# Step 2: Use string formatting to create the mailing address
mailing_address = "{} at {}, {}".format(name, address, zipcode)
# Step 3: Use string methods to clean up the address and zipcode
mailing_address = mailing_address.upper()
# Step 4: Print the final formatted mailing address
print(mailing_address)
#05 changing the values 
name = "Jane Doe"
address = "456 Park Ave"
city = "Mytown"
state = "US"
zipcode = "67890"
address = address.upper()
zipcode = zipcode.upper()
mailing_address = "{} at {}, {} {}".format(name, address, zipcode, state)
print(mailing_address)

