num1 = 0 
num2 = 1 
num3 = 0 

numbers =[0,1]
for i in range (1,100):
	num3 = num2 + num1 
	numbers.append(num3)
	num2,num1 = num1,num2
	num3,num2 = num2,num3



print (numbers)


