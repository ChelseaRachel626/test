str1=input()
str2=input()
count=0
for char in str1:
    if char==str2[-1]:
        count+=1
    else:
        pass
print(count)
