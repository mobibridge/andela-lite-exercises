def sum_of_digits(A):
	c=[]
	sum=[]
	total=0
	for i in range(len(A)):
		c.append(str(A[i]))
	

	''.join(c)

	for s in range(len(c)):
		sum.append(int(s))
		total=total+sum[s]
	return total

	

	
	
	



print(sum_of_digits([10,3]))

