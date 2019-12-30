str="Hello80hi8"
a=str[5]
b=str[9]
c=a+b
print(c)

l=[2,3,4,5,2,3,6,7]
dic={}
for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for key,value in dic.items():
    print(key,value)




