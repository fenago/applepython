#Challenge Lab: Weather Forecasting Company
# Defining the function which will calculate the average temperature
def calculate_average_temperature(temperatures):
    # calculate the average temperature by summing the temperature of each month and dividing by the number of months
    average_temperature = sum(temperatures) / len(temperatures)
    # return the average temperature
    return average_temperature
#initialize the variable which will store the average temperature of each month
average_temperatures = []
#call the function to calculate the average temperature for January
average_temperature_jan = calculate_average_temperature([5,6,7,8,9,10,11,12])
#append the average temperature for January to the average_temperatures list
average_temperatures.append(average_temperature_jan)
#call the function to calculate the average temperature for February
average_temperature_feb = calculate_average_temperature([10,11,12,13,14,15,16,17])
#append the average temperature for February to the average_temperatures list
average_temperatures.append(average_temperature_feb)

#call the function to calculate the average temperature for March
average_temperature_mar = calculate_average_temperature([15,16,17,18,19,20,21,22])
#append the average temperature for March to the average_temperatures list
average_temperatures.append(average_temperature_mar)
#print the average temperature for each month
print("Average temperature for each month:")
print("January: ", average_temperature_jan, "°C")
print("February: ", average_temperature_feb, "°C")
print("March: ", average_temperature_mar, "°C")

