# numbers =[2,3,4,5,6,7,8,9]
# ans =[]
# for i in range(4,101) :
# 	for x in numbers :
# 		if i % x != 0 :
# 			break 
# 	ans.append(i)

# print (ans)

# def print_prime (num):
# list_ = []
# is_prime = True
# for i in range(2, num+1):
# for f in range (2,i):
# if i % f == 0: is_prime = False
# if is_prime == True: list_.append(i)
# is_prime = True

# return list_


def print_prime (num):
	list_ = []
	is_prime = True
	for i in range(2, num+1):
		for f in range (2,i):
			if i % f == 0: is_prime = False
		if is_prime : list_.append(i)
		is_prime = True

	return list_

print(print_prime(5))


