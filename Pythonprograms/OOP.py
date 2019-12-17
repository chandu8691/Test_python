class Bank:
    Bank_name="ICICI"
    ROI=14
    MBL:"mumbai"
    def __init__(self,name,age,phno,email,bal=0):
        self.name=name
        self.age=age
        self.phno=phno
        self.email=email
        self.bal=bal
    def deposit(self,amount):
        amt=self.get_amount()
        self.bal+=amt
        self.success()
    def withdraw(self,amt=0):
        if amt==0:
            amt=self.get_amount()
        if amt>self.bal:
            self.failure()
            print("insufficient funds")
            return
        self.bal=self.sub(self.bal,amt)
        self.success()
    def display(self):
        print(self.name,self.age,self.phno,self.email,self.bal)
    def modify(self,name="",age=0,phno=0,email="",bal=0):
        if name!="":
            self.name=name
        if age!=0:
            self.age=age
        if phno!=0:
            self.phno=phno
        if email!="":
            self.email=email
        self.success()
    @classmethod
    def change_Bname(cls,new=""):
        if new=="":
            cls.Bankname=new
            cls.success()
    @classmethod
    def modify_ROI(cls,new=0):
        if new==0:
            new=cls.get_ROI()
            cls.ROI=new
    @staticmethod
    def success():
        print("transaction success")
    @staticmethod
    def get_amount():
        amount=(int(input("enter amount")))
        return amount()
    @staticmethod
    def failure():
        print("transaction failure")
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def get_ROI():
        new=float(input("enter new ROI"))
        return new
Reeta=Bank("reeta",23,9123123123,"reeta@bata.com",10000)
seeta=Bank("seeta",21,9234234234,"geeta@gmail.com")
Reeta.display()
Bank.display(Reeta)
Reeta.withdraw(2000)
Bank.withdraw(Reeta,2000)
Bank.modify_ROI()
print(Reeta.ROI)

