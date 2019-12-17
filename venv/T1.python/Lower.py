str="python"
str2=''
print(str.islower())
i=len(str)-1
while(i>=0):
    str2=str2+str[i]
    i=i-1
print("reversed string=",str2)
