n1,n2=0,1
count=0
nth=int(input("enter n value "))
if nth<=0:
   print("please enter some positive number")
elif nth==1:
     print(n1)
else:
    print("Fibonacci series")
    while count<nth:
          print(n1)
          n3=n1+n2
          n1=n2
          n2=n3
          count+=1

