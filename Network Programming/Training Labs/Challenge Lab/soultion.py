import requests
import paramiko
import subprocess

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

def sftp_copy(local_file, remote_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("server_ip", username="server_username", password="server_password")
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)
    sftp.close()
    ssh.close()

def remote_access():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("server_ip", username="server_username", password="server_password")
    ssh_shell = ssh.invoke_shell()
    while True:
        command = input("Enter a command: ")
        ssh_shell.send(command + "\n")
        if command == "exit":
            break
        output = ssh_shell.recv(4096).decode()
        print(output)
    ssh.close()

if not check_website():
    send_email("Website down", "The website is currently not reachable.")
    sftp_copy("local_file.txt", "remote_file.txt")
    remote_access()
else:
    print("Website is up and running.")
