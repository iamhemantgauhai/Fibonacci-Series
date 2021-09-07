inp = int(input("Enter number of turns You want for fibonacce >>>> "))

m=0
p=1
print(0)
for i in range(inp -1):
	n=m+p
	print(n)
	p=m
	m=n
