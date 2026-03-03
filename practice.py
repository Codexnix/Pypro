#  -------------- GENERATORS ----------------------

# returns values at one time ,uses yield  , faster than list for big datas


#         return	             yield
#     Ends function immediately	 Pauses function
#     Returns single value	     Returns multiple values over time
#     Function cannot resume	 Function resumes from last point
#     Used in normal functions	 Used in generator functions

# example



def count_up(n):
    for i in range(n):
        yield i
    
gen = count_up(10)
print(next(gen))                  # NEXT shows yielded value 


nums = (x*x for x in range(5))   # lazy eavluation(no returning until required)

for i in nums:                   # i called it thats why return values unless no output
    print(i)


# DECORATORS 

# a function that modifies another function

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hi():
    print("Hi")

say_hi()


# Decorator with arguments

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        result = func(*args, **kwargs)
        print("After function runs")
        return result
    return wrapper

@decorator
def greet():
    print("greet : hello")

greet()