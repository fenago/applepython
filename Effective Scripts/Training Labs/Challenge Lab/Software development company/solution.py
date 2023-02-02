import subprocess
import argparse
import logging
import schedule
import time

logging.basicConfig(filename="file_count.log", level=logging.INFO)

def count_files(dir_path):
    result = subprocess.run(["ls", dir_path, "-1"], capture_output=True, text=True)
    file_count = len(result.stdout.split("\n")) - 1
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    logging.info(f"{current_time}: {file_count} files in {dir_path}")
    print(f"{current_time}: {file_count} files in {dir_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help="Directory to count files in")
    args = parser.parse_args()

    schedule.every().day.at("00:00").do(count_files, args.dir)

    while True:
        schedule.run_pending()
        time.sleep(1)
