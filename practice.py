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