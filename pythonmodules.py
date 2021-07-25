
# tells the operating system
import platform
#x=platform.system()
#print(x)

#list all the defined names belonging to the platform module
#import platform
#x=dir(platform)
#print(x)

#creating a module
#save the below code in a file named mymodule.py...run
#def greeting(name):
#   print("Hello"+name)


#module can contain functions and also varibales of all types(lists,dictionaries and objects)
#how to use the code from mymodule

#mymodule.py

#person1={
#"name":"John",
#"age":36,
#"country":"Norway"
# }



import mymodule
mymodule.greeting("subhra")

a=mymodule.person1["age"]
print(a)

#you can create an alias when you import a module,by using 'as' keyword
import mymodule as mx
a=mx.person1["country"]
print(a)

#import only the person1 dictionary from the module
from mymodule import person1
print(person1["name"])


#datetime module in python
import datetime
x=datetime.datetime.now()
print(x)

#the date contains year,month,day,hour,minute,second and microsecond

#returns the year and name of weekday
print(x.year)
#Weekday
print(x.strftime("%A"))

#month 
print(x.strftime("%B"))

#day of the month
print(x.strftime("%A"))

#year 
print(x.strftime("%Y"))

#for more information search for datetime module in python in w3 schools

#----------------------------------------------------------------------------
#Math module in python(allows you to perform mathematical tasks on numbers)
x=min(5,10,25)
y=max(5,10,25)
print(x)
print(y)

#abs() function returns the absolute positive value of the specified number
x=abs(-7.25)
print(x)

#pow(x,y) function returns the value of x to the power of y
x=pow(4,3)
print(x)

#math module
#math.sqrt() returns the square root of a number
import math
x=math.sqrt(64)
print(x)

x=math.ceil(1.4)#rounds a number upwards to its nearest integer
y=math.floor(1.4)#rounds a number downwards to its nearest integer

print(x)#returns 2
print(y)#returns 1

x=math.pi
print(x)









