str="python"
a=input("enter the string")
print(a)
str2=''
print(a.islower())
i=len(a)-1
while(i>=0):
    str2=str2+a[i]
    i=i-1
print("reversed string=",str2)
