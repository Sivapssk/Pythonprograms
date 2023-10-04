n=int(input())
for i in range(1,n+1):
    print(i,end=' ')
print('\n')
for i in range(n,0,-1):
    print(i,end=' ')
print('\n')
print('even numbers n')
for i in range(2,n*2+1,2):
    print(i,end=' ')
print('\n')
print('odd numbers n')
for i in range(1,n*2+1,2):
    print(i,end=' ') 
print('\n')    
print('sum of n num')
s=0
for i in range(1,n+1):
    s=s+i
print(s)
print('\n')
s=0
print('sum of even numbers')
for i in range(2,n*2+1,2):
    s=s+i
print(s,end=' ')
print('\n')
print('sum of odd numbers')
s=0
for i in range(1,n*2+1,2):
    s=s+i
print(s,end=' ')
print('\n')
s=0
print('sum of even upto n')
for i in range(2,n+1,2):
    s=s+i
print(s)
print('\n')
s=0
print('sum of odd upto n')
for i in range(1,n+1,2):
    s=s+i
print(s)
print('\n')
print('factorial')
f=1
for i in range(n,0,-1):
    f=f*i
print(f)