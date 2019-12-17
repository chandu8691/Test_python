l=[2,5,['hi','hello',5,3],8]
print(l[2][0][1])
l[2].insert(0,'jnfgj')
print(l)


l={"name":'abc',"age":13,"add":{"add1":'hadu',"add2":'kasjk'}}
print(l["add"]["add2"])


#Decorator

def outer(func):
    def inner():
        print("hi")
        func()
    return inner
@outer
def wish():
    print("hello")
wish()

#lambda
z=lambda a,b:a+b
print(z(2,3))