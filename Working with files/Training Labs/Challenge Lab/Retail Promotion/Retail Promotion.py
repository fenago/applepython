code = input("Enter your unique code:")
with open("gift_codes.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if line.strip() == code:
            lines.pop(i)
            found = True
            break
    if found:
        with open("gift_codes.txt", "w") as file:
            file.writelines(lines)
            print("Code successfully redeemed!")
    else:
        print("Invalid code. Please try again.")
