# Step 1: Input number of days overdue
while True:
    days_overdue = int(input("Enter number of days overdue: "))
    # Step 2: Use relational operators
    if days_overdue <= 0:
        print("Book is not overdue, no late fee to be charged.")
        break
    elif days_overdue <= 5:
        # Step 3: Use if and elif statements
        late_fee = 0.5
    elif days_overdue <= 10:
        late_fee = 1
    elif days_overdue <= 30:
        late_fee = 5
    else:
        # Step 4: Use Boolean Operators
        late_fee = 10
    print(f"Late fee to be charged: ${late_fee}")
    # Step 5: Exit the loop
    break
