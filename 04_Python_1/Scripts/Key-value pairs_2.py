import csv
import os.path
titels = ["First name", "Last name", "Job title", "Company"]
ourData = {"First name":input("Enter your first name: "), "Last name":input("Enter your last name: "), "Job title":input("Enter your job title: "), "Company":input("Enter your company: ")}
file_found = os.path.isfile("Our Data.csv")
with open("Our Data.csv", "a") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = titels)
    if not file_found:
      writer.writeheader()
    writer.writerow(ourData)
    csv_file.close()
    

