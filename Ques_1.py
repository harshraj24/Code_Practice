# WAP to inpt 2 nos. sepearated by ',' & find a^b without using '**'
# Input : 2,3
# Output : 8
# Explanation : 2^3
no,power=map(int,input().split(","))
ans=no
for i in range(1,power):
  ans=ans*no
print(ans)
