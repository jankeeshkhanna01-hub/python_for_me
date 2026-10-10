# print("hello world")                //use to print python code


# //variable : memory location to store the data
#a variable is created the moment u assign a value to it 

# python is a dynamically typed language
# age = 34                    #variable decleration  integer
# name="jankeesh "            #string
# cgpa = 7.77                 #float
# rules for variables:
# 1. first letter must be letter not with number
#2. variable names are case seneitive
#3. avoid using python keywords.


#python data-types:
# 1. integer
# 2. float
# 3. string 
# 4.boolean
# 5.lists
# 6.tuples
# 7. sets
# 8. dictonaries

#is_compeleted = True                #t of true must be capital same for false 

# age=2
# print(type(age))                      # to get type of a variable 



#type cating:    changing one dtata type to another 
# a=34
# b="34"
# print(a)
# print(type(a))                     #returns int
# print(b)
# print(type(b))                     #returns str 

# #convert b to a integer

# c=int(b)
# print(type(c))

#
# d=223
# print(d)
# e=str(d)
# print(e)
# print(type(e))
# age= 21
# if(age>19):
#     print("u can vote")

# name =" jankeesh khanna"
# age=21
# print(f" my name is {name} \n and i am {age} y/o")


# print()

# tu = (10,)
# print(type(tu))

# se= {1,2,3,4,5}
# print(se)
# se[0]= 6
# print(se)

# dict={"name":"jankeesh" , "age" : "21" , "year" : "3"}
# print(dict)
# print(dict["name"])



# f = open("jk.txt","r")
# conetent = f.read()
# f.close()
# print(conetent)


# import requests
# req = requests.request('GET', 'https://httpbin.org/get')
# print(req.text)




# class animal:
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed

#     def bark(self):
#         print(f" {self.name} is barking")        



# dog=animal("rafel","poodle")
# dog1=animal("lucy","goldenretriver")

# print(dog.name)
# print(dog1.breed)

# class cat(animal):
#     def __init__(self , name):
#         self.name=name
#     def speak(self):
#         print(" meow ")


# cat1 = cat("kitty")
# cat1.speak()
# cat1.bark()


# def fgh(func  ):
#     def wrapper():
#          print("something is happening")
#          func()
#          print("something had happened")
#     return wrapper



# @fgh
# def say_hello():
#     print(" hello")

# say_hello()    
    


# class person:
#     def __init__(self,name):
#         self.name=name
#     @property
#     def get_name(self):
#         print(self.name)
#     @get_name.setter
#     def set_name(self,new_name):
#         self.name=new_name    

# p1 = person("alice")
# p1.get_name
# p1.name="bob"
# p1.get_name



# try:
#     num=int((input("enter a number ")))
#     result = 10/num
# except Exception as e:
#     print(f" error is :{e}")

