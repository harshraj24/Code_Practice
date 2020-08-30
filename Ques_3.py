# WAP to input n elements in a list & Display the list in the sorted order without using any built in Function
# Input : Harsh Bharati Abhimanyu Abhinav
# Output : Abhimanyu Abhinav Bharati Harsh
def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))

n=int(input())
lst=[]
for i in range (n):
  s=input()
  lst.append(s)
print(quicksort(lst))
