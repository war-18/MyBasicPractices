from ast import Lambda
from itertools import zip_longest


x=10
y=(i**2 for i in range(x+1) if(i%2!=0))

#string concatinate
name="Hello"
print(f"{name} LAmbda")
#Hello LAmbda

# Lamba anonymous function(function without name) 
# can take any number of arguments
#  But return  only one Expression
#One is free to use lambda functions
# wherever function objects are required.

(lambda name:print(f"{name} Gaurav"))("(lamda arg: expr)(string calling)")
z = lambda x,y:x*y
y = lambda z: z+1
print(z(2,10))


#

lmbda=[ lambda x = x:x*x for x in range(1,10)]
for i in lmbda:
    print(i(),end=" ")


#dictionary comprihentions5
dictionary=['0','1','2','4']
newDict=[x for x in dictionary if('0')in x]
print(dictionary)
print(newDict)

sqrt_dict={num:num*num for num in range(1,11)}
print(sqrt_dict)


