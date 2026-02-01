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
        self.__fathername = fname                  # to chnage fname can be changed by adding this function full controll gathered.


adm = Admin('rohan roy ' ,'10', 'kaif roy')
adm.details()
adm.change('rahul roy','rohit roy')
adm.finaldetails()

#----------------------ENCAPSULATION---------------------------------#

