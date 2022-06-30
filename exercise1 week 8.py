# names=["Hind", "Rajaa", "Soaad"]
# ages=[17, 20, 19]
# scores={
#  "math":[ 15, 16, 19],
#  "english":[13,20,17], 
#  "art":[17,10, 19], 
#  "technology":[13,18,18]
#  }
# x = []

# end = {}
# avg = []
# for i in range (len(names)):
# 	total = (scores['math'][i]+scores['art'][i]+scores['english'][i]+scores['technology'][i]) / 4 * 5
# 	print({names[i] :{"age":ages[i], "avg" :total }})
	
# --------------------------------------------------------------
from functools import reduce 
nums = [ i for i in range(44)]
print(reduce(lambda x,y: max (x,y) ,nums ))