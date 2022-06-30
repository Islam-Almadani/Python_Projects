numbers = [1,2,3,4,5,6]

def nums(x):
	x.sort()
	for i in x :
		if i% 2 == 0 :
			if x[i] > x[i-1] :
				
				continue 
			else : 
				x[i] ,x[i-1]= x[-1] ,x[i]
				
		else :
			if x[i] < x[i-1] :
				continue 
			else  : 
				x[i] ,x[i-1]= x[i-1] ,x[i]
	return (x)
print (nums(numbers))
print(len(numbers))


