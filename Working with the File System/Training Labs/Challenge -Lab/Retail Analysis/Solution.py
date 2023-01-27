import os
import shutil
import pandas as pd
import glob


#Check if the "Raw_Data" folder exists, if not create the folder
if not os.path.exists("Raw_Data"):
    os.mkdir("Raw_Data")
#Move all the CSV files in the current directory to the "Raw_Data" folder
for file in glob.glob("*.csv"):
    shutil.move(file, "Raw_Data")
#For each CSV file in the "Raw_Data" folder, perform the following tasks:
for file in glob.glob("Raw_Data/*.csv"):
    #Read the CSV file using pandas
    data = pd.read_csv(file)
    #Remove any rows where the "Quantity" column is less than 1
    data = data[data["Quantity"] > 0]
    #Rename the "Quantity" column to "Units Sold"
    data = data.rename(columns={"Quantity":"Units Sold"})
    #Add a new column called "Total Sales" that is calculated by multiplying the "Units Sold" by the "Price" column
    data["Total Sales"] = data["Units Sold"] * data["Price"]
    #Save the cleaned and transformed data to the same file
    data.to_csv(file, index=False)
#Combine all the cleaned and transformed CSV files into one single file called "Combined_Data.csv" in the current directory
# Initialize an empty DataFrame
combined_data = pd.DataFrame()


# Use glob to find all the cleaned and transformed csv files in the "Raw_Data" folder
for file in glob.glob("Raw_Data/*.csv"):
    # Read the csv file using pandas
    data = pd.read_csv(file)
    # Append the data to the combined_data DataFrame
    combined_data = combined_data.append(data)
# Save the combined data to "Combined_Data.csv" in the current directory
combined_data.to_csv("Combined_Data.csv", index=False)
# Print a message to the console to let the user know that the script has completed successfully
print("Data cleaning and transformation completed successfully. The combined data can be found in 'Combined_Data.csv'.")

