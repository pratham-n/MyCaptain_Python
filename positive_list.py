lst=[]
n=int(input("How many elements? "))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
for num in lst:
    if num>=0:
        print(num, end=" ")
