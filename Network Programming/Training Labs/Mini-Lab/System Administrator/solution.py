import requests
import smtplib

def check_website():
    try:
        response = requests.get("https://www.example.com")
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def send_email(subject, body):
    sender = "sender_email@example.com"
    receivers = ["receiver_email@example.com"]
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.ehlo()
        server.login("sender_email@example.com", "sender_password")
        server.sendmail(sender, receivers, message)
        server.close()
        print("Email sent successfully.")
    except:
        print("Failed to send email.")

if not check_website():
    send_email("Website down", "The website is currently not reachable.")
    # Access the server and fix the issue.
else:
    print("Website is up and running.")
