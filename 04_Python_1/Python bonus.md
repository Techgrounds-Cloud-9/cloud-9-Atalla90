# [Python bonus]

[16 mini code puzzels.]

## Key terminology

[]

## Exercise

1.

Broken code:

~~~
'''
The output should be:
hello Casper
hello Floris
hello Esther
'''
foo = 'hello'
ls = ['Casper', 'Floris', 'Esther']
for name in ls:
 print(loo,name)
~~~

Fixed code: Fixed the variable name in the print statement, from "loo" to "foo"

~~~
foo = 'hello'
ls = ['Casper', 'Floris', 'Esther']
for name in ls:
 print(foo,name)
~~~

2.

Broken code:

~~~
'''
The output should be:
100
'''
foo = 20
bar = '80'
print(foo + bar)
~~~

Fixed code: Converted the variable "bar" in the print statement to an integer

~~~
foo = 20
bar = '80'
print(foo + int(bar))
~~~

3.

Broken code:

~~~
'''
The output should be:
30
'''
foo = 20
for i in range(10):
 foo -= 1

print(foo)
~~~

Fixed code: incremented i instead of decrementing it

~~~
foo = 20
for i in range(10):
 foo += 1

print(foo)
~~~

4.

Broken code:

~~~
'''
The output should be:
there are 0 kids on the street
there are 1 kids on the street
there are 2 kids on the street
there are 3 kids on the street
there are 4 kids on the street
'''
foo = 0
while foo <= 5:
 print('there are', foo, 'kids on the street')
 foo += 1
~~~

Fixed code: foo should be just less than and not equals 5

~~~
foo = 0
while foo < 5:
 print('there are', foo, 'kids on the street')
 foo += 1
~~~

5.

Broken code:

~~~
'''
The output should be:
Star Wars
'''
ls = ['Lord of the rings', 'Star Trek', 'Iron Man', 'Star Wars']
print(ls[4])
~~~

Fixed code: The third index of the list should be printed, not the fourth, since list indices start with 0.

~~~
ls = ['Lord of the rings', 'Star Trek', 'Iron Man', 'Star Wars']
print(ls[3])
~~~

6.

Broken code:

~~~
'''
The output should be:
80
'''
foo = 80
if foo < 30:
 print(foo)
else:
 print('big number wow')
elif foo < 100:
 print(foo)
~~~

Fixed code: Swapped positions between "elif" and "else"

~~~
foo = 80
if foo < 30:
 print(foo)
elif foo < 100:
 print(foo)
else:
 print('big number wow')
~~~

7.

Broken code:

~~~
'''
The output should be:
['Dog', 'Cat', 'Fly']
'''
ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']
short_names = []

for animal in ln:
 if len(animal) == 3:
  short_names.append(animal)
 short_names = []

print(short_names)
~~~

Fixed code: the variable short_names, which contains the list, shouldn't be updated after the loop

~~~
ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']
short_names = []

for animal in ln:
 if len(animal) == 3:
  short_names.append(animal)

print(short_names)
~~~

8.

Broken code:

~~~
'''
The output should be:
20
'''
foo = 10
bar = 2
print(foo**bar)
~~~

Fixed code: The multiplying sign just one asterisk * should be used.

~~~
foo = 10
bar = 2
print(foo*bar)
~~~

9.

Broken code:

~~~
'''
The output should be:
0
1
2
3
4
8
9
'''
for i in range(10):
 if i < 5:
  print(i)
 elif i < 8:
  break
 else:
  print(i)
~~~

Fixed code: The loop should be continued instead of broken

~~~
for i in range(10):
 if i < 5:
  print(i)
 elif i < 8:
  continue
 else:
  print(i)
~~~

10.

Broken code:

~~~
'''
The output should be:
the number is 20
'''
print('the number is' + 20)
~~~

Fixed code: the ingteger 20 should be a string in order for it to be incremented with another string.

~~~
print('the number is ' + '20')
~~~

11.

Broken code:

~~~
'''
The output should be:
IT LIVES!
'''
dev monster():
 print('IT LIVES!')

monster()
~~~

Fixed code: def instead of dev to define a function

~~~
def monster():
 print('IT LIVES!')

monster()
~~~

12.

Broken code:

~~~
'''
The output should be:
4
16129
'''
def square(x):
 return x**2

nr = square(2)
print(nr)

big = square(foo)
print(big)

foo = 127
~~~

Fixed code: The variable "foo" should be declared prior to calling the function on it

~~~
def square(x):
 return x**2

nr = square(2)
print(nr)

foo = 127
big = square(foo)
print(big)
~~~

13.

Broken code:

~~~
'''
The output should be:
Your random number is: <insert random number here>
'''
import random

random.randint(1,100)
print("Your random number is:")
~~~

Fixed code: The random number value should be contained in a variable and that variable should be mentioned as a string in the print statement

~~~
import random

x= random.randint(1,100)
print("Your random number is: " + str(x))
~~~

14.

Broken code:

~~~
'''
The output should be:
True
'''
def rtn(x):
 return(x)

foo = rtn(3)

if foo > rtn(4):
 print(True)
else:
 print(False)
~~~

Fixed code: greater than should be changed to less than

~~~
def rtn(x):
 return(x)

foo = rtn(3)

if foo < rtn(4):
 print(True)
else:
 print(False)
~~~

15.

Broken code:

~~~
'''
The output should be:
a5|||5|||5|||a5|||5|||5|||a5|||5|||5|||
'''
foo = ''
for i in range(3):
 foo += 'a'
 for j in range(3):
  foo += '5'
 for k in range(3):
  foo += '|'

print(foo)
~~~

Fixed code: The third loop should happen within the second one

~~~
foo = ''
for i in range(3):
    foo += 'a'
    for j in range(3):
        foo += '5'
        for k in range(3):
           foo += '|'

print(foo)
~~~

16.

Broken code:

~~~
'''
The output should be:

'''
import random

# generate random int
goal = random.randint(1,100)

win = False
tries = 0

while win == False and tries < 7:
 try:
  # ask for input
  inpt = int(input("Please input a number between 1 and 100: "))
  # count attempt as a try
  tries += 1

  # check for match
  if inpt == goal:
   win = True
   print("Congrats, you guessed the number!")
   print("It took you", tries, "tries")
  # give hints
  elif inpt < goal:
   print("The number should be higher")
  else:
   print("The number should be lower")

 except:
  print("Please type an integer")

# 
if win == False:
 print("Game over! You took more than seven tries")
~~~

Fixed code: Expanding the comment on top of the code to contain the whole code, by moving the second three quotation marks all the way down, will comment the whole code out and give us the blank result we watnt

~~~
'''
The output should be:

import random

# generate random int
goal = random.randint(1,100)

win = False
tries = 0

while win == False and tries < 7:
 try:
  # ask for input
  inpt = int(input("Please input a number between 1 and 100: "))
  # count attempt as a try
  tries += 1

  # check for match
  if inpt == goal:
   win = True
   print("Congrats, you guessed the number!")
   print("It took you", tries, "tries")
  # give hints
  elif inpt < goal:
   print("The number should be higher")
  else:
   print("The number should be lower")

 except:
  print("Please type an integer")

# 
if win == False:
 print("Game over! You took more than seven tries")
'''
~~~

### Sources

[]

### Overcome challenges

[]

### Results

[Script pls fix 1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_01.py)  
[Script pls fix 2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_02.py)  
[Script pls fix 3](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_03.py)  
[Script pls fix 4](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_04.py)  
[Script pls fix 5](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_05.py)  
[Script pls fix 6](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_06.py)  
[Script pls fix 7](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_07.py)  
[Script pls fix 8](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_08.py)  
[Script pls fix 9](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_09.py)  
[Script pls fix 10](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_10.py)  
[Script pls fix 11](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_11.py)  
[Script pls fix 12](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_12.py)  
[Script pls fix 13](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_13.py)  
[Script pls fix 14](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_14.py)  
[Script pls fix 15](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_15.py)  
[Script pls fix 16](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/46cbdb52fcd1e5a2a3e090b116738d5c47f727ed/04_Python_1/Scripts/Pls%20fix_16.py)  

![Pls fix 1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_1.png)
![Pls fix 2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_2.png)
![Pls fix 3](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_3.png)
![Pls fix 4](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_4.png)
![Pls fix 5](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_5.png)
![Pls fix 6](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_6.png)
![Pls fix 7](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_7.png)
![Pls fix 8](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_8.png)
![Pls fix 9](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_9.png)
![Pls fix 10](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_10.png)
![Pls fix 11](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_11.png)
![Pls fix 12](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_12.png)
![Pls fix 13](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_13.png)
![Pls fix 14](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_14.png)
![Pls fix 15](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_15.png)
![Pls fix 16](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/731929f2a4b500a60877d9546cf42461f1d4a35d/00_includes/Python/Pls_fix_16.png)