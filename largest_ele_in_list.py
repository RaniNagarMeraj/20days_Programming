# rand=[8,7,8,5,5,6,7,7,8,444,5,5,6,34]
# rand.sort()
# print(f"{rand[-1]} is the largest")      #it returns largest
# print(rand[0])      #it returns smallest





#without using function
mer=list(map(int,input().split()))

gag=mer[0]
for i in range(len(mer)):
    if mer[i]>gag:
        gag=mer[i]
print(gag)
