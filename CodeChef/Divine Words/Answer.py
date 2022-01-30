a = input()
arr = []
arr.extend(a)
b = int(input())
for i in range(b):
    counter = 0
    brr = []
    c = input()
    brr.extend(c)
    for j in range(len(brr)):
        for k in range(len(arr)):
            if(brr[j] == arr[k]):
                counter+=1
                break
    if(counter == len(brr)):
        print("Yes")
    else:
        print("No")
