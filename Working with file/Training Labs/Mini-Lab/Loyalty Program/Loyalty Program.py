class LoyaltyProgram:
    def __init__(self):
        self.points = 0

    def add_points(self, points):
        if points>0:
            self.points += points
    def check_points(self):
        if self.points > 100:
            return "Gold status"
        else:
            return "Regular status"
            
    def update_file(self):
        with open("loyalty_points.txt", "r") as file:
            lines = file.readlines()

        for i in range(len(lines)):
            customer_info = lines[i].split()
            if customer_info[0] == self.name:
                self.add_points(int(customer_info[1]))
                customer_info[1] = str(self.points)
                customer_info.insert(1, self.check_points())
                lines[i] = " ".join(customer_info) + "\n"
                break
        else:
            lines.append(self.name + " " + str(self.points) + " " + self.check_points() + "\n")

        with open("loyalty_points.txt", "w") as file:
            file.writelines(lines)
        
    def __str__(self):
        return self.name + " has " + str(self.points) + " points and " + self.check_points() + " status."
        
#Example Usage
customer1 = LoyaltyProgram()
customer1.name = "John Doe"
customer1.add_points(150)
customer1.update_file()
print(customer1)

customer2 = LoyaltyProgram()
customer2.name = "Jane Smith"
customer2.add_points(50)
customer2.update_file()
print(customer2)
