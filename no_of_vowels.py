#to know number of vowels in a string


str1="All meraj silver tea cups".lower()
count=0
for i in str1:
    if i =="a" or i=="e" or i=="o"or  i=="i"  or i=="u":
            count=count+1
print(count)


'''''
str1="All meraj silver tea cups".lower()
count=0
for i in str1:
    if i in 'aieou':
            count=count+1
print(count)'''''