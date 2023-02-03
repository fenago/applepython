import sys
import os
import zipfile
import math
import random
import datetime
import csv
from email.mime.base import MIMEBase
from email import encoders

# Step 1: Import the necessary modules
import sys
import os
import zipfile
import math
import random
import datetime

# Step 2: Get the directory path from the user
arc_dir = input("Enter the directory where the zipped archive files are located: ")
out_dir = input("Enter the directory where the processed data and report will be saved: ")
arc_path = os.path.join(arc_dir, "sales_data.zip")
out_path = os.path.join(out_dir, "sales_report.csv")

# Step 3: Extract the data from the archive files
with zipfile.ZipFile(arc_path, "r") as archive:
    archive.extractall(out_dir)
    archive.close()

# Step 4: Process the data
with open(out_path, "r") as file:
    data = csv.reader(file)
    #skip header
    next(data)
    sales = [float(row[3]) for row in data]
    total_sales = math.fsum(sales)
    avg_sales = total_sales / len(sales)
    max_sales = max(sales)
    min_sales = min(sales)
    
# Step 5: Generate the report
with open(out_path, "w") as file:
    report = csv.writer(file)
    report.writerow(["Total Sales:", total_sales])
    report.writerow(["Average Sales per Day:", avg_sales])
    report.writerow(["Day with Highest Sales:", max_sales])
    report.writerow(["Day with Lowest Sales:", min_sales])
    
# Step 6: Send the report via email
import smtplib

sender_email = "sender@example.com"
receiver_email = "receiver@example.com"
password = "your_password"

message = f"Subject: Sales Report\n\nAttached is the sales report for the month."

with open(out_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment", filename="sales_report.csv")
    msg.attach(part)

server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()

# Step 7: Test the program
test_data = [random.randint(0,1000) for i in range(30)]
print(test_data)
#run the program with the test_data
#verify that the report is generated correctly
