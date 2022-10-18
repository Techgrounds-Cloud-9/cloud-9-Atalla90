# [Data types and comments]

[Getting to know different data types supported in Python and how to write comments.]

## Key terminology

[Data type: A certain kind of value that a processor can deal with in a certain way, meaning that a data type determines what for operations can be done on that data.

String: A data type. A sequence of characters, usually represents a textual value.

Integer: A data type. A numerical value used only to represent a whole number.

Float: A data type. A numerical value that can be used to represent a fraction.

Boolean: A data type. It has only one of two values, either True or False.

None: A data type. It represents the absence of any value.

Comment: A line in the code that doesn't get proccessed as code, and is used for explanation purposes.]

## Exercise

1. Determined the data types of the given values, created a new variable and tried to contain the sum of b and d in it, which was not possible until converted d to a flaot as follows:

~~~
#Copying the variables and their initial values as stated in the exercise
a = "int"
b = 7
c = False
d = "18.5"

#Printing the type of each current value contained in each variable using the type() method
print (type(a))
print (type(b))
print (type(c))
print (type(d))

#Creating the variable x that contains the value of b + d using the float() and printing its output
x = b + float(d)
print (x)
~~~

2. Created a variable that stores user's input. Found out that user's input in python is always a string. I did that using the following code:

~~~
name = input ("Name: ")
print (type(name))
age = input ("Age: ")
print (type(age))

age = int(age)
print (type(age))
~~~

### Sources

[1. <https://en.wikipedia.org/wiki/String_(computer_science>)

2. <https://www.freecodecamp.org/news/integer-definition/#:~:text=An%20integer%20is%20a%20positive,floats%2C%20short%2C%20and%20long>.

3. <https://www.freecodecamp.org/news/boolean-definition/#:~:text=In%20computer%20science%2C%20a%20boolean,value%20of%20false%20is%200>.]

### Overcome challenges

[]

### Results

[Script 1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/1ceec9e4c5cc31c4308ef5860d3c15b42723b3c3/04_Python_1/Scripts/Data%20types%20and%20comments_1.py)  
[Script 2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/1ceec9e4c5cc31c4308ef5860d3c15b42723b3c3/04_Python_1/Scripts/Data%20types%20and%20comments_2.py)

![Data_types_1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/888a1e0e94e0f251534a4b8916ea60aa372219e5/00_includes/Python/Data_types_1.png)
![Data_types_2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/888a1e0e94e0f251534a4b8916ea60aa372219e5/00_includes/Python/Data_types_2.png)
