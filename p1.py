x= "100"
y= int(x)
z= str(100)
i=float(x)
j=bool(x)
print(type(x))
print(type(y))
print(type(i))
print(type(j))
print(j)

#bool 100 is true because any non zero no. in python treted as true


# lets say talking about grades normal way(LOOPS NORMAL)

ii=int(input("enter the no. :- "))

 
if ii>90:
    print('a')
elif ii>80:
    print('b')
elif ii>70:
    print('c')
elif ii>60:
    print('d')
else:
    print('e')


#  Short hand trick for if else (Used for )

grade='A' if ii>90  else 'b' if ii>80 else 'c' if ii>70 else 'd' if ii>60 else 'e'
print (grade)

#(IMP) PRE REQUISTS FOR LOOPS

#break      -- exit loop
#continue   -- skip iteration
#pass       -- do nothing


#for loop question
#The Task: Write a for loop that processes a list of mixed sensor readings: readings = [25.5, "ERROR", 30.2, -999, 45.1, "NULL", 28.7]
#Filter: Create a new list that only includes valid float numbers.
#Threshold: If a number is negative (like -999), ignore it—it’s a sensor glitch.
#Aggregation: Calculate the total sum of the valid, positive numbers.
#Early Exit: If the total sum exceeds 100, stop the loop immediately and print: "Limit Reached."
#ANSWER
rd = [25.5, "ERROR", 30.2, -999, 45.1, "NULL", 28.7]
sum=0
l1=[]

for i in rd:
    if type(i)!=float:
        pass
    elif i<0:
        pass
    else:
        l1.append(i)
        sum+=i
        
        if sum>100:
            print('limit reached')
            break

print('New List ', l1 )


# WHILE LOOP QUESTION

#The AI Training Simulator
#Imagine you are training a model. You want it to reach an accuracy of 90%, but training is unpredictable.
#The Task: Write a while loop that simulates training an AI:
#Start with accuracy = 50.0.
#In each iteration (representing an "epoch"), generate a random float between -5.0 and 10.0 and add it to the accuracy.
#Boundary Logic: Accuracy cannot go above 100 or below 0. (If it goes to 102, set it back to 100).
#The "Stagnation" Rule: Keep track of how many iterations have passed. If the accuracy hasn't reached 90 after 15 iterations, break the loop and print: "Training Failed: Stagnation."
#If it hits 90 or higher before then, print: "Model Trained!"



# the answer

# REMEMBER IN WHILE ELSE ALSO CAN BE COMBINED BUT THAT ELSE CONDITION WILL ONLY 
# BE SHOWED IF WHILE RUNNED NATURALLY WITHOUT ANY BREAK

import random
A=50.0
i=0
while i<15:
    i+=1
    num=random.uniform(-5.0,10.0)
    A=A+num
    if A>100:
        A=100
    elif A<0:
        A=0
    if A>90:
        print(A)
        print('model trained')
        break
else:
    print('Model training failed no stagnation rule followed iterations limit reached')

# BASIC FUNCTION

def add(a,b):
    print('addtion give nos. ' ,a+b)
a=int(input('enter the 1st. no :-  '))
b=int(input('enter the 2nd. no :-  ')) 
add(a,b)

# Types of arguments in functinons

def sub(a=10,b=20):   # Defualt argument always mentioned while defining function
    print(a-b)
sub()
sub(b=10,a=15)         # keyword argument mentioned while calling

def ARGS(*n):          # *Args  argument 
    print(n)
ARGS(10,20,30,40,50)

# Output :  (10, 20, 30, 40, 50)

def keywargs(**kwargs):          # SIMPLE KWARGS EXAMPLE (**)COMPLUSORY
    print(kwargs)

keywargs(ayush=20,rahul=40)

# OUTPUT :  {'ayush': 20, 'rahul': 40}

def Kwargs(**n):                 # KWARGS EXAMPLE WITH FOR LOOP 
    for key,value in n.items():
        print(key,"scored this no.",value)

Kwargs(ayush=20,rahul=40,rajn=20)


#   ayush scored this no. 20          (OUTPUT)
#   rahul scored this no. 40
#   rajn scored this no. 20


# lambda function

square= lambda x:print(x*x)
square(10)

# lambda function done by Map

Data=[1,2,3,4,5,6,7,8]
multipesoncealone=list(map(lambda x:x*20 ,Data))
print(multipesoncealone)

# Lambda function done by filter

smallerthanfive=list(filter(lambda x:x<5,Data))
print(smallerthanfive)

# Lambda Function done by sorted

Datas=[(1,2),(2,4),(2,5)]
sorting=sorted(Datas,key=lambda x:x[1])         # sorted whole DATAs set by their each element second position
print(sorting)

#Output
#100
#[20, 40, 60, 80, 100, 120, 140, 160]
#[1, 2, 3, 4]
#[(1, 2), (2, 4), (2, 5)]


# list

l2=[1,2,3,4,5,6,7,8,9,10]

l3=[1,2,3,4,5,6,7,8,9,10]

l3.append(11)                  #list functions
print(l3)                      # append,insert,remove,pop,reverse,sort,clear,count,index
l3.remove(3)
print(l3)
l3.insert(2,20)
print(l3)
l3.pop(-3)
print(l3)
print(l3.count(10))
print(l3)
print(l3.index(10))
l3.clear()
print(l3)
l1.reverse()
print(l1)
l1.sort()
print(l1)

# OUTPUT

#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#  [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
#  [1, 2, 20, 4, 5, 6, 7, 8, 9, 10, 11]
#  [1, 2, 20, 4, 5, 6, 7, 8, 10, 11]
#  1
#  [1, 2, 20, 4, 5, 6, 7, 8, 10, 11]
#  8
#  []
#  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# LIST COMPREHENSION

nums=[1,2,3,4,5,6,7,7,8,9,9,0,1,10]
l1=[x*x for x in nums]            # normal lis comprehnsion
print(l1)
l1.sort()

l2=[x for x in l1 if x%2==0 ]     # list comprehnsion with filter
print(l2)

l3=['pass' if i>50 else 'fail' for i in l1]  # list comprehnsion with  if-else way
print(l3)

# OUTPUT 

#  [1, 4, 9, 16, 25, 36, 49, 49, 64, 81, 81, 0, 1, 100]
#  [0, 4, 16, 36, 64, 100]
#  ['fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'pass', 'pass', 'pass', 'pass']

# Dictionary 

Dict={'ayush':20,'rahul':30}

#  ACCESSING WAYS
print(Dict['ayush'])   # value 
Dict.get('ayush')

# Modify

Dict['ayush']=30
print(Dict)
#marks updated 

# FOR LOOP FOR DICT

for key,value in Dict.items():
    print(key,value)


# dictionary Comprehension

sq= {x*x for x in range(5)}
print(sq)

# 20
# {'ayush': 30, 'rahul': 30}
# ayush 30
# rahul 30
# {0, 1, 4, 9, 16}

# OOPS 


class hello :
    amount = 1000
    def hi(self,name):
        print('hi your brother',name)
    def salary(self,amount):
        print('hello , what is your salary?  ,my salary :-- ',amount)
    def brother(self):
        print('what is your name bro')

c1= hello()

c1.hi('rahul')

c1.salary(2000)

c1.brother()


# AS FUNCTIONS ARE ACESSING SAME WAY ATTRIBUTES CAN BE ACCESSED

# EXAMPLE  (IN ABOVE THE AMOUNT OF SALARY MENTIONED BY AMOUNT VARIABLE ) ,which can be accessed by 

print(c1.amount)                   # this will print c1 .amount


# Now making functions odd and even 

class odd_even:
    l=[1,2,3]
    def odd(self,l):
        l1=[]
        for i in l:
            if i%2!=0:
                l1.append(i)
            else:
                pass
        print(l1)

    def even(self,l):
        l1=[]
        for i in l:
            if i%2==0:
                l1.append(i)
            else:
                pass
        print(l1)   

ops= odd_even()

ops.even([1,2,3,4,5,6,7,7,8])                     # EVEN
ops.odd([1,2,3,4,5,6,7,8,9,10,11,12])             # ODD

# By including intialistion method (init)


class odd_even_o:
    def __init__(self,l):
        self.l = l


    def odd(self):
        l= self.l
        l1=[]
        for i in l:
            if i%2!=0:
                l1.append(i)
            else:
                pass
        print(l1)

    def even(self):
        l=self.l
        l1=[]
        for i in l:
            if i%2==0:
                l1.append(i)
            else:
                pass
        print(l1)   

ops1= odd_even_o([1,2,3,4,5,6,7,8,89])                   # here we can provide data
ops1.even()
# then ask operation

# ops1.odd(l)          name 'l' is not defined (error found  to solve take below step)

#  l=self.l         (in every corner)


op2=odd_even_o([1,2,3,4,5,6,7,8,9,0,11,21,2,2,33,44])

op2.odd()

# now machine opeartion

class Machine:

    def __init__(self,name,function,itertions):
        self.machine_name= name                  # YOU CAN ALSO FIX THE VALUE OF NAME BY CHAING VALUE OF NAME WITH STRIGN VALUES 'NAME'
        self.function_name= function             # SIMILARY LIKE ABOVE , YOU CAN ASSIGN FIXED VALUE VALUES FOR FUNCTION AND ITERATION COUNT
        self.iterations_count= itertions

    def extract_machine(self):
        print(self.machine_name,self.function_name)

    def extract_iterations(self):
        print(self.function_name,'iteration count :-- ',self.iterations_count)

M1= Machine('Megatech','rounding','15')

M1.extract_machine()
M1.extract_iterations()

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