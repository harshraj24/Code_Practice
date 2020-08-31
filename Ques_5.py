#bubble sort
n=input()
lst=n.split(",")
k=[]
for i in lst:
    k.append(int(i))
l=0

while l < len(k):
    j=0
    while j<l:
        if k[l]<k[j]:
            #swap
            temp=k[l]
            k[l]=k[j]
            k[j]=temp
        j=j+1
    l=l+1
print(k)
