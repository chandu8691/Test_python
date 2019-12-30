str="chandana"
x=""
for i in str:
    x=i+x
    if(str==x):
        print("is a palindrome")
else:
    if(str!=x):
        print("not a palindrome")

print(len(str))
s=str[::-1]
print(s*3)

