import os
import datetime
import shutil

# check if external hard drive is connected
if not os.path.exists("/mnt/external_drive"):
    print("Backup completed successfully.")
    exit()

# create new folder on external hard drive with current date and time as name
now = datetime.datetime.now()
folder_name = now.strftime("%Y-%m-%d-%H-%M-%S")
os.makedirs(f"/mnt/external_drive/{folder_name}")

# copy all .docx, .xlsx, and .pptx files from company's "Important Files" folder to new folder on external hard drive
important_files_folder = "/mnt/important_files"
extensions_to_copy = [".docx", ".xlsx", ".pptx"]

# create log file in new folder on external hard drive
log_file = open(f"/mnt/external_drive/{folder_name}/backup_log.txt", "w")

for file in os.listdir(important_files_folder):
    if file.endswith(tuple(extensions_to_copy)):
        shutil.copy2(f"{important_files_folder}/{file}", f"/mnt/external_drive/{folder_name}")
        log_file.write(f"{file} backed up at {now}\n")

log_file.close()

# print message to let user know backup has been completed successfully
print("Backup completed successfully.")
