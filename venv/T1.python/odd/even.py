i=1
if i%2==0:
    print("even")
else:
    print("odd")

def oddeven(A):
    even=[]
    odd=[]
    for i in A:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("even",even)
    print("odd",odd)

A = [2, 5, 13, 17, 51, 62, 73, 84, 95]
oddeven(A)
    
