n=int(input("Enter the number:"))
count=0
while count<=n:
    a=2
    p=0
    for i in range(2,a-1):
        if a%i is 0:
            p=p+1
        if p==0:
            s=1
            for i in range(a,0,-1):
                s=s*i
                print(s)
    count=count+1
    

            
