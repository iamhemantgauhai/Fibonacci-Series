inp = int(input("Enter number of turns You want for fibonacce >>>> "))
print(0)
m=0
p=1

for i in range(inp -1):
	n=m+p
	print(n)
	p=m
	m=n