#######################oops####################
#oops-
#4 pillars of oops
#data abstraction,polymorphism,encapsulation,inheritance
#access specifier->it specfier the access to retrieve data
#access modifier->public,private,protected
###class####
'''class myclass:
    def add(a,b):#inside class->method,outside class->funtion
        return a+b
#creating object
obj1=myclass#add,sub,mul is methods
print(obj1.add(2,5))
obj2=myclass
print(obj2.add(2,7))'''
#7
#9
'''class myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mod(a,b):
        return a%b
    def mul(a,b):
        return a*b
obj1=myclass
print(obj1.add(2,5))
obj2=myclass
print(obj2.add(2,5))
print(obj2.mul(2,7))'''
#########constructor#########
'''class myclass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mod(a,b):
        return a%b
    def mul(a,b):
        return a*b
obj1=myclass
print(obj1.add(2,5))
obj2=myclass
print(obj2.add(2,5))
print(obj2.mul(2,7))'''
#class variable#
'''class myclass:
    cls_var="im class variable"#can be used in all method of class'''
############inheritance##########
#single inheritance
'''class animal:
    def speak():#method
        return "animal is speaking"
    #single ineitance
class dog(animal):
    def bark():
        return "bow........."
obj1=animal#object
print(obj1.speak())
obj2=dog
print(obj2.bark())'''
#mutilevel ineitance
'''class animal:
    def speak():#method
        return "animal is speaking"
    #single ineitance
class dog(animal):
    def bark():
        return "bow........."
class puppy():
    def puppy_speak():
        return "puppy is speaking"
obj1=animal#object
print(obj1.speak())
obj2=dog
print(obj2.bark())
obj3=puppy
print(obj3.puppy_speak())'''
#multiple ineitance
'''class Father:
    def Father_speak():
        return "father class"
class Mother:
    def Mother_speak():
        return "Mother class"
class Kid(Father,Mother):
    def kid_speak():
        return "in kid. im haveing properties of father and mother"
obj1=Kid
print(obj1.kid_speak())
print(obj1.Father_speak())
print(obj1.Mother_speak())'''
#polymorphism -->
#method overriding
'''class Animal:
    def speak():#method
        return "animal is speaking"
    #single ineitance
class Dog(Animal):
    def bark():
        return "bow........."
class Puppy(Dog):
    def Puppy_speak():
        return "puppy is speaking"
obj1=Puppy#object
print(obj1.Puppy_speak())'''
'''def run():#returns running fast(i.e the latest one)and running is lost
    return "running"
def run():
    return "running fast"
print(run())'''
#####methed over loading#######
'''class cal:
    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        return (sum)
obj1=cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
#3
#6
#10'''
 

        


    




        
       
    
        