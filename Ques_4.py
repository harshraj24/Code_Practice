# WAP to enter n datas of students in a dictionary and diplay the 2nd position student with their average
# Input :  3
#          Harsh 20 30 60
#          Bharati 50 90 70
#          Abhimanyu 60 90 80
# Output : Bharati 70.00
n = int(input())
sum=0
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    student_marksi={}
    student_marksi[name]=scores
k=[]
for i,j in student_marks.items():
    lst=j.copy()
    summation=(lst[0]+lst[1]+lst[2])/3
    k.append(summation)
l=sorted(k)
t=l[1]
for i in range(len(k)):
    if k[i] == t:
        print(i,student_marks.items())
