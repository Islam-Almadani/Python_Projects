def triangle (a,b,c) : 
	if a + b <= c : 
		print ("this cant be a triangle")
	elif a + c <= b : 
		print ("this cant be a triangle") 
	elif b + c <= a : 
		print ("this cant be a triangle")
	else : 
		print ("this can be a triangle")

def Right_angled (a,b,c): 
	if a > b and a > c:
		if b*b + c*c == a*a :
			print ("its a Right-angled triangle")
		else : 
			print ("its not Right-angled triangle")
	if b > a and b > c:
		if a*a + c*c == b-b :
			print ("its a Right-angled triangle")
		else : 
			print ("its not Right-angled triangle")
	if c > b and c > a:
		if b*b + a*a == c*c :
			print ("its a Right-angled triangle")
		else : 
			print ("its not Right-angled triangle")

def Equilateral_triangle (a,b,c): 
	if a==b and b==c : 
		print ("its Equilateral triangle") 
	else : 
		print ("its not Equilateral triangle")

Equilateral_triangle(6,6,6)
Right_angled(3,4,5)
triangle(1,2,3)