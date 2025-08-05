name=input("enter your name:")
name=name.lower()
rev=name[::-1]
if rev==name:
    print("palindrome")
else:
    print("not palindrome")