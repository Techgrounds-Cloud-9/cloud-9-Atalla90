#importing csv module
import csv
'''
importing os.path module to check the file's path. 
That way we can write the headers only once when creating
the file if it doesn't exist, otherwise we only append the
new user's input to the file as a new row without the headers.
'''
import os.path
#Creating a list containing the headers
titels = ["First name", "Last name", "Job title", "Company"]
ourData = {"First name":input("Enter your first name: "), "Last name":input("Enter your last name: "), "Job title":input("Enter your job title: "), "Company":input("Enter your company: ")}
file_found = os.path.isfile("Our Data.csv")
#Opening the csv file in append mode
with open("Our Data.csv", "a") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = titels)
    if not file_found:
      writer.writeheader()
    writer.writerow(ourData)
    csv_file.close()
    

