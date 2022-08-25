def fib(n):
    a,b=0,1
    if(n==0):
        return a
    if(n==1):
        return b
    else:
        # return fib(n-1)+fib(n-2)
        for i in range(2,n+1):
            ans=a+b
            a=b
            b=ans
        return b
        
def main():
    n=int(input())
    for i in range(n+1):
        print(fib(i),end=" ")
    print(fib(n))


if __name__ =="__main__":
    main()
