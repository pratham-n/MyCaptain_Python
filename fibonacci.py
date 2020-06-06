nterms=int(input("How many terms? "))
n1=0
n2=1
count=0
if nterms<=0:
    print("Enter positive integer!")
elif nterms==1:
    print("Fibonacci series is: ")
    print(n1)
else:
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
