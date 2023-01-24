import smtplib
 
# function to send email
def send_email(recipient, subject, body):
	try:
    	# create an SMTP object to connect to the email server
    	server = smtplib.SMTP('smtp.gmail.com', 587)
    	# start the TLS (Transport Layer Security) encryption
        server.starttls()
    	# login to the email server
        server.login("your_email@gmail.com", "your_password")
    	# compose the message
    	message = f"Subject: {subject}\n\n{body}"
    	# send the message
    	server.sendmail("your_email@gmail.com", recipient, message)
    	# close the server connection
    	server.quit()
        print("Email sent successfully!")
	except smtplib.SMTPAuthenticationError:
        print("Authentication Error: Invalid Email or Password")
	except smtplib.SMTPConnectError:
        print("Connection Error: Unable to connect to the email server")
	except Exception as e:
        print("Error:", e)
	finally:
        print("Closing email server connection...")
 
# get user input for recipient, subject, and body
recipient = input("Enter the recipient's email address: ")
subject = input("Enter the subject: ")
body = input("Enter the message body: ")
 
# call the function to send the email
send_email(recipient, subject, body)

