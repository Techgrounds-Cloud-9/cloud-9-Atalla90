# [Key-value pairs]

[Getting used to key-value pairs (dictionaries) in Python.]

## Key terminology

[Key-value pair: a general concept meaning linking two elements together, so that one of them becomes a reference (key) to the other (value).

Dictionary(Dict): A built-in key-value pairs data structure in Python. The pairs in a dict are contained between curly brackets {}, with a colon separating each key and value and with each pair separated from the other with a comma. As of Python 3.7, dictionaries in Python are ordered, though keys in a dictionaries can't be duplicated. It's also referred to as a mapping data structure, as it maps keys to values. The same data structure is referred to as "Hash table" or "Hash map" in other programming languages.

CSV file: Comma Separated Values; a document that contains a list of data in rows with comma's separating the elements.]

## Exercise

1. Created a dict using the given data, looped over it and printed the key-value pairs as follows:

~~~
x = {"First name:" : "Casper", "Last name:": "Velzen", "Job title:": "Lead Learning Coach", "Company:": "TechGrounds"}
for i in x:
    print(i,x[i])
~~~

2. Created a dict using data from user's input and wrote it to a CSV file as follows:

~~~
#importing csv module
import csv
'''
importing os.path module to check the file's path. 
That way we can write the headers only once when creating
the file if it doesn't exits, otherwise we only append the
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
~~~
The output in the CSV file looks as follows:

~~~
First name,Last name,Job title,Company

Mo,Atalla,Student,TechGrounds

Karim,Touzani,Student,TechGrounds
~~~

### Sources

[1. <https://www.w3schools.com/python/python_dictionaries.asp>

2. <https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/>

3. <https://www.codingem.com/python-write-to-csv-file/>]

### Overcome challenges

[]

### Results

[Script 1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/e12eb273c834fd1e3dd5907a5cefb4433130b55e/04_Python_1/Scripts/Key-value%20pairs_1.py)  
[Script 2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/e12eb273c834fd1e3dd5907a5cefb4433130b55e/04_Python_1/Scripts/Key-value%20pairs_2.py)  
[CSV file](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/e12eb273c834fd1e3dd5907a5cefb4433130b55e/04_Python_1/Scripts/Our%20Data.csv)

![Key-value_pairs_1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a117cb89a519411761b32eda8a11a958593cde58/00_includes/Python/Key-value_pairs_1.png)
![Key-value_pairs_2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a117cb89a519411761b32eda8a11a958593cde58/00_includes/Python/Key-value_pairs_2.png)
![CSV](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a117cb89a519411761b32eda8a11a958593cde58/00_includes/Python/CSV.png)
