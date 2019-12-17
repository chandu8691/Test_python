f=open("test1.txt","r")
a=f.read(1)
print(a)
f.close()

#read from file and print unique letters
f=open("asg1.txt","w")
f.write("it is a python class\n it is a java class")
f=open("asg1.txt","r")
r=f.read()
w=r.split()
unique=set(w)
for w in unique:
    print(w)

'''f=open("asg1.txt","r")
r=f.read()
s=reverse(r)
for i in s:
    print(i)'''

#find average of num
def Average(list):
    return sum(list)
list=[2,4,6,8,10]
average=Average(list)
print("average of list=",average)

#Armstrong number
num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==num:
    print("nuum is armstrong number")
else:
    print("num is not a armstrong number")

#print numbers divisible by given num
for i in range(1,10):
    if i%2==0:
        print("the numbers divisible by 2 =",i)


#Marks of 5 students and display the grade
a=int(input("enter the marks in english"))
b=int(input("enter the marks in kannada"))
c=int(input("enter the marks in maths"))
d=int(input("enter the marks in science"))
e=int(input("enter the marks in social"))
avg=((a+b+c+d+e)/500)*100
if(avg>=80):
    print("first class",avg)
elif(avg>=60 and avg<80):
    print("second class",avg)
elif(avg>=40 and avg<60):
    print("third class",avg)

#count no of digits
num=65789
count=0
while (num>0):
    num=num//10
    count=count+1
print("num of digits",count)

#simple intrest
p=10
t=13
r=23
SI=(p*t*r)/100
print("simple intrest",SI)

#return the largest and 2nd largest num
l=[23,77,48,98,46,34]
l.sort()
print(l[-1])
print(l[-2])

#swap 1st and last num
def swaplist(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return newlist
newlist=[12,46,23,67,30]
print(swaplist(newlist))

#count no of words,char and replace blank space with _
s="Today is sunday"
print(s)
newstr=s.replace(" ","_")
print(newstr)
w=len(s.split())
print("the number of words:=",str(w))
count=0
for i in s:
    if i=='s':
        count=count+1
print("no of characters=",str(count))

#lenth of the string
def len(str):
    count=0
    for i in str:
        count+=1
    return count
str="python"
print(len(str))

s="hello"
print(len(s))

#take first 2 and last two char and create a new string
def string_both_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

#add key value pair to dict
dict = {'key1': 'Have', 'key2': 'a'}
print("Current Dict is: ", dict)
dict1 = {'key3': 'Good', 'key4': 'day'}
dict.update(dict1)
dict.update(newkey1='portal')
print(dict)

#find key exits in dict
def checkKey(dict, key):
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not presennt")
dict = {'a': 100, 'b': 200, 'c': 300}
key = 'b'
checkKey(dict, key)
key = 'w'
checkKey(dict, key)

#max,min
s1=[23,24,67,85,21,65,44]
print(max(s1))
print(min(s1))

#random numbers and append to list
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res
num = 10
start = 20
end = 40
print(Rand(start, end, num))

#count vowles
def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)
string = "Geeks for Geeks"
vowels = "AeEeIiOoUu"
Check_Vow(string, vowels);

f=open("test1.txt","r")
a=f.read(1)
print(a)

#find longest string
f.open("text1.txt","r")
words=file.read().split()
print(words)
print(max(words,key=len))
























