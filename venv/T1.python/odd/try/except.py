'''a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
try:
    c=a/b
    print("the division of a={0} and b={1}".format(a,b),c)
except ZeroDivisionError:
    print("denominator should not be zero")

#assertion
b=12
assert b!=0,"false"
print("true")

#custom exception
class AgeInvalidError(Exception):
    pass
try:
    if age>=18:
        print("valid age==>
    else:
raise:'''

#Has a relation
class car():
    color="red"
    brand="maruthi"
    def fun(self):
        print("the colorr:",self.color)
        print("the brand of the car:",self.brand)
class engine():
    c=car()
    c.fun()


