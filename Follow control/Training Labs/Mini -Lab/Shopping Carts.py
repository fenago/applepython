Follow control /Training Labs/Mini -Lab/ Shopping Carts.py
# Step 1: Limiting the number of items in a shopping cart
# get the number of items entered by the customer
items = int(input("Enter the number of items you want to add to your cart: "))
# assign the allowed limit of items
limit = 50
# check if the number of items entered is greater than the allowed limit
if items > limit:
    # display a message to the customer that they have exceeded the limit
    print("You have exceeded the limit of", limit, "items. Please enter a new number of items.")
    items = int(input("Enter the number of items you want to add to your cart: "))
# Step 2: Adding items to the cart
# use a while loop to keep prompting the customer to add items to their cart until they reach the limit
while items < limit:
    # get the number of items entered by the customer
    add_items = int(input("Enter the number of items you want to add to your cart: "))
    items += add_items
    # display the current number of items in the cart and the remaining items that can be added
    print("Current number of items in the cart:", items)
    print("Remaining items that can be added:", limit - items)
# Step 3: Checkout or continue shopping
# get the customer's choice
choice = input("Do you want to continue adding items to the cart? (y/n) ")
# check if the customer's choice is "n" (no)
if choice == "n":
    # exit the while loop
    break

# Step 4: Proper white space
# use proper white space and indentation to make your code readable and easy to understand
# Step 5: Alternate ways to exit a loop
# use other ways to exit a loop such as the continue statement
# use the continue statement to skip the current iteration of the loop and move on to the next iteration
if items >= limit:
    continue
# use the print() function to print the status
print("Status:", items, "items in the cart.")
