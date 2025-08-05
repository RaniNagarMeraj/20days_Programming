name=input("enter your name:")
rev=""
for i in name:
    rev=i+rev
if rev==name:
    print("palindrome")
else:
    print("not a palindrome")