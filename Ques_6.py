#Fibonacci Series
#with Greater no
n=int(input())
fibo=1
if(n<=0):
    print("Invalid NO")
k=[]
for i in range(1,n+1):
    fibo=fibo*i
    k.append(fibo)
print(k[-1])
