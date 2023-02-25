import csv
import random

with open("abalone.csv", "w", newline="") as csvfile:
    fieldnames = ["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(1000):
        sex = random.choice(["M", "F", "I"])
        length = round(random.uniform(0.1, 0.9), 2)
        diameter = round(random.uniform(0.1, 0.9), 2)
        height = round(random.uniform(0.1, 0.9), 2)
        whole_weight = round(random.uniform(0.1, 1.9), 2)
        shucked_weight = round(random.uniform(0.1, 1.0), 2)
        viscera_weight = round(random.uniform(0.01, 0.5), 2)
        shell_weight = round(random.uniform(0.01, 0.5), 2)
        rings = random.randint(1, 29)
        writer.writerow({
            "Sex": sex,
            "Length": length,
            "Diameter": diameter,
            "Height": height,
            "Whole weight": whole_weight,
            "Shucked weight": shucked_weight,
            "Viscera weight": viscera_weight,
            "Shell weight": shell_weight,
            "Rings": rings
        })
