# #print ([i if i%2==0 else "Odd" for i in range(10)])
# #print ([ letter for letter in 'Python class' ])
#
# #iterator
# a=[2,4,5,7]
# i=iter(a)
# print(next(i))
# print(next(i))
#
# class Hotel():
#     def__init__(self)
#         self.menu=['assad','bdas','cftsrf']
#         self.index=-1
#     def__iter__(self)
#         return self
#     def__next__(self)
#     self.index+=1
#         if self.index>=len(self.menu):
#             raise:StopIteration
#         return self.menu[self.index]
# for in in hotel()
#     print(i)
#
#
# #yield(generator)
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#         yield f
# for i in fact(5):
#     print(i)

num=[34,66,23,2,5]
z=list(map(lambda x:x%2==0,num))
print(z)