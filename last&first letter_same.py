#negative indexing
name=input("enter your name:")
name=name.lower()
if name[0]==name[-1]:
    print("Lucky")
else:
    print("super lucky")

#using len
# name=input("enter your name:")
# name=name.lower()
# if name[0]==name[len(name)-1]:
#     print("lucky")
# else:
#     print("super lucky")
