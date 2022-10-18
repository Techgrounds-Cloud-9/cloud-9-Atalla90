# [Conditions]

[Getting familiar with conditional statements in Python.]

## Key terminology

[Conditional: A statement that's used to test for the presence of a certain condition and based on that directs a part of the code to one direction or the other. A condetional in Python can be implemented using "if.. else" statements of "if.. elif.. else" statements.]

## Exercise

1. Created a condetional statement to test if the user's input matches my name using the following code:

~~~
name = input("What's your name? ")
if name == "Atalla":
    print("Hey me!")
else:
    print("You're not me. Please leave my script alone")
~~~

2. Created a conditional statement to test if the user's input less than, greater than or equals 100 using the following code:

~~~
while True:
    num = input("Hit me with a num: ")
    num = int(num)
    if num < 100:
        print("Try higher")
    elif num > 100:
        print("Try lower")
    else:
        print("Hold on right there!")
        break
~~~

### Sources

[1. <https://www.guru99.com/if-loop-python-conditional-structures.html#:~:text=What%20are%20Conditional%20Statements%20in,by%20IF%20statements%20in%20Python>.]

### Overcome challenges

[]

### Results

[Script 1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/3fb75d3dce0c6e88aa157a39b52c0f1af7538e06/04_Python_1/Scripts/Conditions_1.py)  
[Script 2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/3fb75d3dce0c6e88aa157a39b52c0f1af7538e06/04_Python_1/Scripts/Conditions_2.py)  
![Conditions_1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/e8f2abf8607a56d19542aefb2ea2af95a2c2ceb5/00_includes/Python/Conditions_1.png)
![Conditions_2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/e8f2abf8607a56d19542aefb2ea2af95a2c2ceb5/00_includes/Python/Conditions_2.png)