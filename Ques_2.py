# WAP to input an array seperated by space ' ' and find it's 2nd max item without using max Function
# Input : 1 3 4 2 5 8 6 6 4 9 8
# Output : 8
n=input()
lst=n.split(" ")
li=[]
for i in lst:
    li.append(int(i))
print(list(sorted(list(set(li))))[-2])
