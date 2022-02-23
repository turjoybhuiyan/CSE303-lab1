def Fibonacci(n):
   if n<=0:
      print("Fibonacci can't be computed")
   elif n==1:
      return 0
   elif n==2:
      return 1
   else:
      return Fibonacci(n-1)+Fibonacci(n-2)
n=int(input("Enter Number "))
print("{}th Fibonacci number is ".format(n),Fibonacci(n))