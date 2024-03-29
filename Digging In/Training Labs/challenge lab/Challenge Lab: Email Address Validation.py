#Lab challenge solution 
# Step 1: Prompt the user for an email address
#step 1 
import re
email = input("Enter an email address: ")
# Step 2: Use regular expressions to check that the email address meets the criteria
# The email address must contain the @ symbol
# The email address must end with a valid domain, such as .com, .edu, or .gov
# The email address must not contain any spaces
# The email address must not contain any special characters, except for the @ symbol and the period (.)
email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|edu|gov)"
# Step 3: Print the appropriate message for a valid or invalid email address
if re.match(email_regex, email) and "@" in email and " " not in email and re.search(r"[^a-zA-Z0-9@.\s]",email)==None:
    print("Valid email address")
else:
    print("Invalid email address")
