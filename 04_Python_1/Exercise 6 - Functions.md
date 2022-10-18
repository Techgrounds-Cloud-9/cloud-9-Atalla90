# [Functions]

[Getting used to using the bulit-in functions and methods in Python as well as creating self-made functions.]

## Key terminology

[Function: A set of instructions that perform a certain task and gets created to be called (used) later in one specific or in several codes. Functions are generally used to return some value.

Method: A function that is related to an object and always passes it as an argument. It may or may not return a value.

Parameter: A variable that plays the role of a place holder for the argument that has to be passed into a function when the later gets called in order for it to perform its task.

Argument: The value the function needs to be provided with when it gets called in order for it to perform its task.

Library: A library of saved codes that can be imported and used in Python. A library contains smaller units called "Packages". A package contains even smaller and more specific units called "Modules".

Frame work: A library that contains packages and modules that make up the architecture of an application.]

## Exercise

1. Imported "random" library and printed 5 random numbers between 1 and 100 as follows:

~~~
import random
a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
d = random.randint(1,100)
e = random.randint(1,100)
print (a)
print (b)
print (c)
print (d)
print (e)
~~~

2. Wrote a function that prints a string to a terminal, and then rewrote it to take a string as an argument and prints to the terminal as follows:

~~~
def myfunction():
    print("Hello, world")
myfunction()

def myfunction(x: str):
    print("Hello,", x)
myfunction("Atalla")
~~~

3. Wrote a function that returns the average of its parameters and used it on the variables in given code as follows:

~~~
def avg(x:float, y:float):
    av = (x+y)/2
    return av
    
x = 128
y = 255
z = avg(x,y)
print ("The average of",x,"and", y, "is", z)
~~~

### Sources

[1. <https://www.geeksforgeeks.org/difference-method-function-python/#:~:text=Functions%20can%20be%20called%20only,are%20dependent%20on%20that%20class>.

2. <https://www.w3schools.com/python/python_functions.asp>

3. <https://learnpython.com/blog/python-modules-packages-libraries-frameworks/#:~:text=A%20library%20is%20an%20umbrella,and%20other%20packages%20(subpackages>).]

### Overcome challenges

[]

### Results

[Script 1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/bc032e58bbc7f52d56c32f85c417b6aa950c7105/04_Python_1/Scripts/Functions_1.py)  
[Script 2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/bc032e58bbc7f52d56c32f85c417b6aa950c7105/04_Python_1/Scripts/Functions_2.py)  
[Script 3](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/bc032e58bbc7f52d56c32f85c417b6aa950c7105/04_Python_1/Scripts/Functions_3.py)

![Functions_1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/48c0ba6c034c200e7d25a73afd7bab51e18bd3e5/00_includes/Python/Functions_1.png)
![Functions_2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/48c0ba6c034c200e7d25a73afd7bab51e18bd3e5/00_includes/Python/Functions_2.png)
![Functions_3](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/48c0ba6c034c200e7d25a73afd7bab51e18bd3e5/00_includes/Python/Functions_3.png)
