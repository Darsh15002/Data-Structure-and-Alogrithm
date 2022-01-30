a = int(input())
for i in range(a):
	arr = []
	brr = []
	b = input()
	c = input()
	arr.extend(b)
	brr.extend(c)
	counter = 0
	if(len(arr)==len(brr)):
		for j in range(len(arr)):
			if(arr[j]==brr[j]):
				continue
			elif(arr[j]=='?'or brr[j]=="?"):
				continue
			elif(arr[j]!=brr[j]):
				print("No")
				counter+=1
				break
		if(counter==0):
			print("Yes")
	else:
		print("No")
