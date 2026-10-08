# LC factorial 1
import math 
print(math.factorial(5))
def times(factors):
   return factors*2
factors=range(1,11)
print(*factors)
def times(products):
   products = map(times, products)
products=[]
for factor in factors:
   
   products.append(factor)
   
print(*products)

while True:
    try:
      users_input = int(input('what number do you want the factorial of(1-10) :'))
    except: 
      print("thats not a number fool")
    else: 
        if 0 <= users_input:
           break
        else:
           print("thats a negitve number fool")
products.append(list(map(math.factorial, factors)))
print(*products)




