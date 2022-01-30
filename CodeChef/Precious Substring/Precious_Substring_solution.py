a = int(input())
while(a!=0):
	b = int(input())
	c = input()
	arr=[]
	arr.extend(c)
	counter = 0
	for i in range(len(arr)):
		if(arr[i]=="1"):
			counter+=1
		else:
			continue
	brute = (counter*(counter-1))//2
	answer = counter+brute
	print(answer)
	a-=1