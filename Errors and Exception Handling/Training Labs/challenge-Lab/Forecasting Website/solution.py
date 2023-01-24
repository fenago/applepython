import smtplib
import requests

def get_weather(location):
    # Make API call to weather service to get weather information for the location
    try:
        response = requests.get(f'https://weather-service.com/{location}')
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as e:
        print(f'An error occurred: {e}')
        return None

def send_weather_update(recipient, location, subject):
    weather_data = get_weather(location)
    if weather_data:
        body = f"Weather update for {location}:\n\n"
        body += f"Temperature: {weather_data['temperature']} degrees F\n"
        body += f"Conditions: {weather_data['conditions']}\n"
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
            print("Weather update sent successfully!")
        except smtplib.SMTPAuthenticationError:
            print("Authentication Error: Invalid Email or Password")
        except smtplib.SMTPConnectError:
            print("Connection Error: Unable to connect to the email server")
        except Exception as e:
            print("Error:", e)
    else:
        print("Error: Unable to get weather data for the provided location.")

# get user input for recipient, location, and subject
recipient = input("Enter the recipient's email address: ")
location = input("Enter the location: ")
subject = "Daily Weather Update"

try:
    send_weather_update(recipient, location, subject)
except smtplib.SMTPAuthenticationError:
    print("Invalid Email or Password. Please try again.")
except smtplib.SMTPConnectError:
    print("Unable to connect to the email server. Please check your internet connection and try again later.")
except Exception as e:
    print("An error occurred. Please try again later.")
