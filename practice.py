#------------OOPS CONCEPTS AND INTIALISATION ALSO BASICS CLASSES AND OBJECTS-------------


class Admin:
    
    def __init__(self,name,classes,fathername):                   # here basically i am blocking the updates of fathername this shows encapsulation of data
        self.name = name
        self.classes = classes
        self.__fathername = fathername
    
    def details(self):
        print(self.name , self.classes,self.__fathername)

    def change(self,k,n):
        self.name = k
        self.classes = n
        print('new name = ',self.name,'new classess : ' ,self.classes)

    def finaldetails(self):
        print(self.name , self.classes,self.__fathername)

#-------------------------------------------------------------------------------------------------------------

#  TWO CONCEPTS IMP FOR ENCAPSULATION IS SETTER WITH VALIDATION AND GETTER 

# 1. GETTER (GETTING THE ENCAPSULATED DATA )

# IN ABOVE PROCESS YOU CAN'T GET THE DETAILS OF ENCAPSULATED DATA TO GETT IT WE WILL ADD ONE FUNCITON

    def __getstate__(self):
        print(self.__fathername)

# 2. Setter with Validation       
    def change_fname(self,fname):                  # whole process is encapsulated above but still if you want
        if not isinstance(fname,str):
            print('data type not right')
            return                                 # return needed to go back to caller
        
        if len(fname)<3:
            print('name to short try again') 
            return
        
        self.__fathername = fname 
        print('fname changed succesfully')            # to chnage fname can be changed by adding this function full controll gathered.


adm = Admin('rohan roy ' ,'10', 'kaif roy')
adm.details()
adm.change_fname(10)
adm.finaldetails()
adm.change_fname('rahulroy')
adm.finaldetails()

#-----------------------------------ENCAPSULATION---------------------------------#

# 2nd topic 

#----------------------INHERITANCE(PARENT-CHILD RELATIONSHIP(IS - A))-------------#

class User:
    def login(self):
        return  'logic'

class admin(User):
    def hello(self,hello):
        self.hello = hello
        print('hello ' ,self.login() ,self.hello)

k=admin()
k.hello('rahl')

#for more explanation refer notes
#-----------------INHERITANCE----------------------------------------#

#---------------POLYMORPHISM-----------------------------------------#

# SAME METHOD DIFFERENT USE

class User:
    def role(self):
        return "User"

class Admin:
    def role(self):
        return "Admin"

def print_role(user):
    print(user.role())

print_role(User())
print_role(Admin())

# here WE ARE USING SAME ROLE FUNCITON BUT FOR DIFFERENT USE IN DIFFERENT CLASSESS.

#  for more explanations refer notes.

#------------POLYMORPHISM---------------------#

#------------ABSTRACTION(RULES)---------------#

#strict rules for all funcitons having parent child should have required or fixed abstract(funcitons fixed by this method) funcitons

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print('paid ',amount,' amount credited via UPI ')
    
upiid=UPI()
upiid.pay('5000')

#fixing the pay function to be must in any class where payment is parent child so that must ip funcitons will not be missed

# FOR MORE REFER NOTES

#-----------ABSTRACTION-------------------------------#


#----------COMPOSITTION-------------------------------#

# HAVING (HAS-=A) RELTATION NOT LIKE INHERITANCE(IS - A)  

# PREFEREED FOR FLEXIBILTY 

# ONE CLASS USE ANOTHER CLASS

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

engine=Car()
engine.engine.start()

# for more expalantion refer notes

#-------------------COMPOSITION-----------------#

#----------METHOD OVERIDING --------------------#

#CHILD CLASS PARNET METHOD
#INHERTITANCE IMP

class User:
    def role(self):
        return "User"

class Admin(User):
    def role(self):
        return "Admin"


# for more refer notes

#-------------method overiding------------------#

#---------SOLID PRINCIPLES----------------------#

# Most imp to revise are only 3 SOD

# 1. S — Single Responsibility Principle (SRP)

# one class = one job 

# -----------------bad implementation--------------------------------#
class User:                                        
    def save(self): pass
    def send_email(self): pass

# ------------ Right implemenatiton ----------------------------------#
class UserRepository:                          
    def save(self): pass

class EmailService:
    def send(self): pass


# make code clean and properly usable 


# 2. O — OPEN / CLOSED PRINCIPLE (OCP)

# EXTENSION OF FUCNTIONS WITHOUT LOOSING OLD CODE OR EDITING (make old code usable not useless)

# -------------------- BAD EXAMPLE---------------------------#


def pay(amount, method):
    if method == "upi":
        print("Paid via UPI")
    elif method == "card":
        print("Paid via Card")


# ------------------RIGHT EXAMPLE ----------------------------#

class Payment:
    def pay(self, amount):
        pass
class UPI(Payment):
    def pay(self, amount):
        print("Paid via UPI")
class Card(Payment):
    def pay(self, amount):
        print("Paid via Card")
def process_payment(payment, amount):
    payment.pay(amount)


# RIGHT BECAUSE PROPELY DEFINED AND IN PLACE OF IF-ELSE IT USES DIFFERENT CLASSES FOR DIFFERENT WORK


# 3. D — DEPENDENCY INVERSION PRINCIPLE (DIP)

# High-level modules should not depend on low-level modules.
# Both should depend on abstractions.


#----------------------BAD EXAMPLE -----------------------#

class MySQLDatabase:
    def save(self, data):
        print("Saved to MySQL")
class OrderService:
    def __init__(self):
        self.db = MySQLDatabase()

# BAD EXAMPLE BECAUSE IT  HAS NOT DIRECT ACESSS AND CONNECTIONTO DATABASE

#-------------------GOOD EXAMPLE -----------------------------#

class MySQLDatabase:
    def save(self, data):
        print("Saved to MySQL")
class MongoDatabase:
    def save(self, data):
        print("Saved to MongoDB")
class OrderService:
    def __init__(self, database):
        self.db = database

    def place_order(self, order):
        self.db.save(order)
mysql = MySQLDatabase()
mongo = MongoDatabase()

order1 = OrderService(mysql)
order2 = OrderService(mongo)

order1.place_order("Order A")
order2.place_order("Order B")


# HERE WE HAVE DIRECT ACESS TO DATABASE AND DATA ALSO 



# ABOVE ARE THE ALL IMPORTANT TOPICS AND CODE FOR OOPS UNDERSTANDING AND JOB READY LEVEL



#--------------------------OOPS (END)---------------------------------------#


