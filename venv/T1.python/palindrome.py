str="malayalam"
x=""
for i in str:
    x=i+x
    if(str==x):
        print("is a palindrome")
print(len(str))
s=str[::-1]
print(s*3)

