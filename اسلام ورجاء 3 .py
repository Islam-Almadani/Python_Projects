miles = [3,4,1,2]

progress_days = 0

for i in range (len(miles)-1) :
	print (i)
	if miles[i] < miles[i+1] :
		progress_days += 1 
	else :
		continue 

print (progress_days)
