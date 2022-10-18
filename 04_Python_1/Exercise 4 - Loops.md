# [Loops]

[Getting to know the different ways to implement loops in Python.]

## Key terminology

[Loop: A sequence of code instructions that's meant to be conditionally repeated once, several times or infinitely. In Python there are two types of loops; "For loops" and "While loops".

For loop: Repeats the sequence of instructions for certain number of times determined with a certain range.

While loop: Repeats the sequence of instructions while a certain condition is present.]

## Exercise

1. Used a While loop to print the value of x in every iteration as follows:

~~~
x = 0
while x <= 10:
    print (x)
    x += 1
~~~

2. Printed the value of i. In this case, the iteration in the range of 10 indices is what determined the value of i in every iteration. i here is like a track keeper of the loop. Then created the variable x and multiplied it with the value of i for 50 iterations as follows:

~~~
x = 5
for i in range(10):
    print(i)

x = 5
for i in range(51):
    print(i*x)
~~~

3. Looped over the given array (list) of names and printed each name using the following code:

~~~
arr = ["Coen", "Casper", "Joshua", "Abdessamad", "Saskia"]
for i in arr:
    print (i)
~~~
    
### Sources

[1. <https://www.thoughtco.com/definition-of-loop-958105>]

### Overcome challenges

[]

### Results

[Script 1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/2ad8478464e595f123cac6a3f6bd31895984db04/04_Python_1/Scripts/Loops_1.py)  
[Script 2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/2ad8478464e595f123cac6a3f6bd31895984db04/04_Python_1/Scripts/Loops_2.py)  
[Script 3](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/2ad8478464e595f123cac6a3f6bd31895984db04/04_Python_1/Scripts/Loops_3.py)
![Loops_1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/5e87fdbce509ee1a4b813525603390a5471ae654/00_includes/Python/Loops_1.png)
![Loops_2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/5e87fdbce509ee1a4b813525603390a5471ae654/00_includes/Python/Loops_2.png)
![Loops_3](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/5e87fdbce509ee1a4b813525603390a5471ae654/00_includes/Python/Loops_3.png)
