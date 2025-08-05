n=int(input("enter a number:"))
is_prime=True
for i in range(2,n):
    if n%i==0:
        is_prime=False
print("prime number"if is_prime==True else"not prime")
      
