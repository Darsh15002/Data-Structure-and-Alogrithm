a = int(input())
while(a!=0):
	b,c = map(int,input().split())
	counter = 1
	answer =0
	arr=[]
	while(counter<=c):
		answer = b % counter
		arr.append(answer)
		counter+=1
	print(max(arr))
	a-=1
