t=1,2.0,"Tupple"
s=(1,2.0,"Tupple")
# //Both are same
print("t and s are same :",t is s)#t and s are same : True

print(s , t ,sep="    ")#seperator  #(1, 2.0, 'Tupple')    (1, 2.0, 'Tupple')

print(s[0],t[0])#1 1

#slicing
s= [s[1:]]
print(s[0:1])# [(2.0, 'Tupple')]
print(type(s))  # <class 'list>


#tuples in list

lst= [(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five")]
