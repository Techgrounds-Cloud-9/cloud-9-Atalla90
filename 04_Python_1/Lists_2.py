arr = [34, 50, 121, 94, 29]
for i in range(len(arr)):
    if i != 4:
       print(arr[i]+arr[i+1])
    else:
        print(arr[i]+arr[0])  