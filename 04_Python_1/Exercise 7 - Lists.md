# [Lists]

[Getting used to Python's lists (arrays)]

## Key terminology

[List: A built-in data structure in Python. An ordered sequence of values contained between square brackets [] and separated by comma's. The values in a list are accessible through their indices in the list, starting with 0, and can be duplicated in the same list. The same data structure is called in most other languages "Array".

Set: A built-in data structure in Python. An unordered set of values contained between curly brackets {} and separated by comma's. As the values in a set are not ordered, they have no indices and can't be accessed that way. For the same reason (and also unlike lists), sets don't support duplication of values.

Tuple: A built-in data structure in Python. An ordered sequence of values contained between round brackets (). Tuples can't be modified once made. Since the values are ordered, they can be accessed through their indices and can be duplicated.]

## Exercise

1. Created a list of names, looped over it and printed the names as follows:

~~~
arr = ["Karim", "Daphne", "Tanuja", "Atalla", "Jan"]
for i in arr:
    print (i)
~~~

2. Created a list of integers that gets looped over adding each value to the value that comes after it, except for the last value that gets added to the first one, and printing each sum. The code goes as follows:

~~~
arr = [34, 50, 121, 94, 29]
for i in range(len(arr)):
    if i != 4:
       print(arr[i]+arr[i+1])
    else:
        print(arr[i]+arr[0])
~~~

### Sources

[1. <https://www.w3schools.com/python/python_lists.asp#:~:text=%2C%20%22cherry%22%5D-,List,with%20different%20qualities%20and%20usage>.

2. <https://www.w3schools.com/python/python_tuples.asp>

3. <https://www.w3schools.com/python/python_sets.asp>]

### Overcome challenges

[]

### Results

[Script 1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/d03957b1fb9dbec8a46c6de37c2b98b6cbedb2db/04_Python_1/Scripts/Lists_1.py)  
[Script 2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/d03957b1fb9dbec8a46c6de37c2b98b6cbedb2db/04_Python_1/Scripts/Lists_2.py)

![Lists_1](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/713f4af11301bdedbfe2401420eaccbb9ce93fae/00_includes/Python/Lists_1.png)
![Lists_2](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/713f4af11301bdedbfe2401420eaccbb9ce93fae/00_includes/Python/Lists_2.png)
