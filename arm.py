def armstrong(n):
    temp=n
    sum=0
    while(temp>0):
        d=temp%10
        sum+=d**3
        temp//=10

    if(sum==n):
        return True
    return False

def find_nearest_small_value(key, sorted_li):
    return max(i for i in sorted_li if i >= key)

def main():
    n=1000
    arr=[0]*5
    idx=0
    
    for i in range(1,n):
        if(armstrong(i)):
            arr[idx]=i
            idx+=1
    N=344
    print(arr)
    print(find_nearest_small_value(N,arr))



if __name__ == "__main__":
    main()
