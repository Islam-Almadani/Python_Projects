number = int(input("enter the secands number : "))
scands =0
minits = 0
hours = 0 

while True :
  if number >= 3600 :
    hours = int(number/3600)
    number =number % 3600
  elif number >= 60 :
    minits = int(number / 60) 
    number = number % 60

  elif number <60 :
    scands = number 
    break

print (hours , ":", minits , ":",scands)
