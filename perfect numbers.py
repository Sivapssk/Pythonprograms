n=int(input())
sum=0
for i in range(1,n+1//2):
        if(n%i==0):
                sum=sum+i
if(sum==n):
        print('perfect number')
else:
        print('no')