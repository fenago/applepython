import subprocess
import argparse
import logging

def gather_info(path):
    hostname = subprocess.run(["hostname"], stdout=subprocess.PIPE, text=True).stdout.strip()
    ip = subprocess.run(["hostname", "-I"], stdout=subprocess.PIPE, text=True).stdout.strip()
    uptime = subprocess.run(["uptime"], stdout=subprocess.PIPE, text=True).stdout.strip()
    
    with open(path, "w") as file:
        file.write(f"Hostname: {hostname}\n")
        file.write(f"IP Address: {ip}\n")
        file.write(f"Uptime: {uptime}\n")
        
    logging.basicConfig(filename=f"{path}.log", level=logging.INFO,
                        format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logging.info(f"System information gathered and stored in {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gather system information and store it in a file.")
    parser.add_argument("path", help="Path to store the information.")
    parser.add_argument("-v", "--verbose", help="Print detailed information", action="store_true")
    args = parser.parse_args(["-h"])

    
    gather_info(args.path)
    if args.verbose:
        with open(args.path, "r") as file:
            print(file.read())
