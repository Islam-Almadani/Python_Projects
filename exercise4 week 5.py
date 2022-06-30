def tt(x) :
	tatal = 0 
	y = 0 

	for i in range(x,1,-1):
		if x != 0 :
			if tatal == 0 :
				tatal = x * (x-1)
			else:
				tatal = tatal * (x-1)
			x = x - 1
			# print (tatal , x)
	return tatal 

print (tt(5)) 

