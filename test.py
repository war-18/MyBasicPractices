#GCD

def fact(factNum):
    ans=0
    for i in range(1,factNum+1):
        ans=factNum*i
    # while(i>0):
    #     factNum=factNum*i 
    #     i-=1
    print(factNum)

num = input("Enter a number to find factorial of it: ")
def recur_factorial(n):
    if n == 1 or n==0:
        return 1
    elif n < 1:
        return ("Not Allowed")
    else:
        return n*recur_factorial(n-1)
print (recur_factorial(int(num)))

def prime(N):
    i=2
    arr=[True for i in range(N+1)]
    while(i*i <=N):
        if(arr[i] == True):
            for j in range (2**i,N+1,i):
                arr[j]=False
        i+=1
    arr[0]=False
    arr[1]=False
    
    for i in range(N+1):
        if(arr[i]==True):
            print(i,end=" ")

x=10
prime(x)

fact(x)

#factorial, prime, GCD, largest in list
#
