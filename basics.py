# print function 

# print ("hello babua")

# print(5)

# print (False)

# print("india", "russia", "china")
# # india russia china   the space in btween the words is beacause of thr sep= '/' parameter

# print("india :", 45)

# print("hello", end =' ' )
# print("world")

# datatypes

# # integer
# print(24222222222222222222222222222222222222222222222222222)
# # range is so much big as like (1e308) is the range
# print(1e309)
# inf then it shows infinity 10 to the power 309 zero 


# Float 

# print(4.5)
# print(1.7e308) is the range for the floor 

# print (1e309) the it show u the inf

# boolean 

# print(True)
# print(False)

# String 
# print("kolkata", "tamilnadu")

# print          ("happy")


# # Container type 
# # List 
# print ([1,3,4,5,6])

# # tuple

# print((1,23233,3,4))

# # sets
# print({1,2,3,4,55})

# # dict 
# print({"ayush":12, "mango":43})

# Comments
# cooment is the word that cannot read by the compiler thats it enhance the readability

#c lang 
# int a = 5

# name = "nitesh"
# print (name)

# kaam_kya_hai_bhaiya = "kaam to kuch ni hai bus tumko pareshan krne aaye hai hai hum "
# print(kaam_kya_hai_bhaiya)

# no variable declaration in the python 

# 1 dynamic typing 
# 2 static typing

# python me dynamic typing hi milta hai 

# name =2
# print (name) 
# name = True
# print(name)
# name = "meranaambambu bhaiya"

# print(name)

# this feature is called dynamic binding koi bhi datatype ek variable me store ho jata hai easily 
# python will automatically deduce 

# Static Binding hota hai c and c++ ye hectic hai 

# a= 5; b=2; c=5.3
# print(a)
# print(b)
# print(c)


# special declarartion syntax 
# a,b,c =1,2,3
# print(a)
# print(b)
# print(c)

# a=b=c=6
# print(a)
# print(b)
# print(c)

# keywords and identifiers

# python is the case sentive lang 
# keywords

# it is the reserved word int nhe programming language these are the high level language

# import keyword

# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# identiers

# identifiers is the name to identify a variable, function, class or ther objects

# 1. only start with alphabet or _underscore
# 2. followed by 0or more leeter _or diggit
# 3. keyword cannot be used as identifiers

# First_name = "nittu"
# _babakya23 = "shinchan"
# print(First_name)

# # no special case 
# 1213name = "ayush"
# invalid decimal literal

# False = "False"
# cannot assign to False

# user input 

# for the dynamic  software  we req input 

# name = input("apna naam bata: ")
# print (name)

# first_num = input("enter the first num: ")
# sec_num = input("dusra batao bhaiya: ")
# print(first_num  +  sec_num)


# yahan par kya hora hai string concatination hora hai add krne ke liye type conversion use krna hoga

# Type/
# print(type([1,2,3,4,5]))


# type conversion 
# simple process to use to change the data type 

# 2 types 
# 1. implicit conversion 
# 3+4.5
# 7.5
# >>> 445+224
# 669
# >>> 34+4.5 
# 38.5



# type conversion is not the permanent conversion 


# 2. explicit type conversion 
# >>> str(5)
# '5'
# >>> complex(4)
# (4+0j)
# >>> list("hello")
# ['h', 'e', 'l', 'l', 'o']
# >>> bool(1)
# True
# >>> float(4)
# 4.0

# Literals

# numeric literal 
# string literal 
# boolean literal
# special literal 

# 1 numeric literals

# a = 01010  binary literals
# b = 100 decimal literal 
# c = 0c320 Octal literals
# d = 0x12c hexaadecimal literal 


# 2. string literal 

# string = 'nfkvf'
# multiline = '''v jkvjvk
# nkekekkrkkr'''
# unicode = u"u0001f600"
# print(unicode)

# name = 'ahgj'
# print(name)

# raw_str = r"vkvrkj"

# 3. Boolean literal 

# true false 

# 4. special literal 
# a= None 
# print(a)

# operators in python 

# Arithmetic operators 
# +,-,//,/,**,%

# compariison operatos 
# <,>,<=,>=,==
# logical 
# and , or , not 
# bitwise 
# binary value pe kaam krte hai 

#                         010
# apply &operator on both 110 
#                  Ans -> 010
# 1. x&y
# 2. x|y
# 3. x>>y 
# 4. x<<y 

# assignment 
# +=, -=, *=, /=, %=
# a =3

# identity

# koi do var same memory location par hai ya ni 
# a= "hello"
# b= "hello"

# print (a is b)
# True

# 2. is not 

# memborship operator

# koi cheej dusri chhej uske andar hai ya ni 
# x = "Delhi"

# print("D" not in x)
# False

# in, not in 

# if else statement decision control statements

# top to bootom 
# but in case of branching u req if else statement 






# email = input("apna email batao re bhaiya: ")
# password = input("apna password bhi bata")

# if email == "ayushgautam2007.kg@gmail.com" and password == "123345":
#     print("welcome")
# elif email == "ayushgautam2007.kg@gmail.com" and password != "1234":
#     password = input("password firse bol ")
#     if password=="1234":
#         print("finally correct")
#     else:
#         print("still incorrect kya karra hai be ")
    

# else:
#     print("incorrect credential")


# indentation 

# if(name== 'xyz'){
#     something;
#     something;

# }else{
#     something else;
#     something else;
# }
# yahan ye sab panchayatt ni hai tumhra python already itna hosiyar hai ki usey indentation dena hai bus 

# name = "fkeree"
# if name == "xyz":
#     print("vnjvjv")
#     print("fvekvv")
#     if 5==44:
#         print("agli line")
#     else:
#         # something to sahi hoga na 

# python creators more focused on the code redability isliye saahi se code do hit the tab button to check the correction 

# loops kaha use hotey hai 

# while loop 
# for loop 

# 2 loop bus hotey hai 

# number = int(input("enter the num: "))

# i=1
# while i<12:
#     print(number * i)
#     i+=1

# num = int(input("enter the number you wanteed to enter : "))
# i=1
# while(i<11):
#     print(num,"*",i ,"=" , num*i)
#     i=i+1


# guessing number game 


# num = 83
# i=1
# print(input("chal guess kar: "))
# while(i == 83):
#     i+=1
    
#     if(num<83):
#         print("guess higher number: ")
#     else:
#         print("guess lower number ")

