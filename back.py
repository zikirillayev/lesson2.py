# i = 1
# while i < 101:
#     print(i)
#     i += 1


# x =True
# while x:
#     fruit = input("fruit name")
#     if fruit == "stop":
#         x = False
#     else:
#         print(f"name = {fruit}")


# summa = 0
# while True:
#     n = input("sonni kiriting  \n:")
#     if n == "stop":
#         break
#     n = int(n)
#     summa += n
# print(summa)

# for i in range(10):
#     if i % 2 == 1:
#         continue
#     else:
#         print(i)


# print(round(1.234,2))
# print(pow(2,10))
# print(max(1,2,3,4,5))
# print(min(1,2,3,4,5,6,7,8,9))
# print(sum([1,2,3,4,5,6]))
# import math
# import os 
# print(os.path)


# import random 
# print(random,random()
# print(random.randint(0,10))
# print(random.randint(0,10,2))
# arr = [1,2,3,4,5,6,7,8,9,]
# random.shuffle(arr)
# print(arr)
# str = "assalomualaykum"
# print(random.sample(str,5))


# print(random.sample(range(300),5))

# arr = [1,2,3,4,5,6,7,8,9]
# print(random.choice(arr))

# s = "Python"
# print(s[0],s[1],s[2],s[3],s[4],s[5])
# print(s[::-1]) #reverse

# me = "saidali"
# we = "team"
# you = me[:4]
# print(we + you)

# r = "length"
# # print(len(r))
# print(r.strip("l")) #ength
# print(r.rstrip("h")) #lengt
# print(r.lstrip("l")) #ength
# print(r.split(" "))
# print(r.rsplit(" "))
# print("".join(["s" , "saf"]))

# print(r.upper())
# print(r.lower())
# print(r.capitalize())
# print(r.title())

# w = "e f jhsdbvhjsbjdnfvbshbudifhewuidvs"
# print(w.find("e"))
# print(w.index("h"))
# print(w.count("e"))

# print(w.startswith("e"))
# print(w.endswith("s"))
# print(w.replace("e" , "w"))

# q = "sakfmskvd12213"  #checkers __________
# print(q.isalnum()) # only number and word
# print(q.isalpha()) # only word
# print(q.isdigit()) # only number 
# print(q.isnumeric()) # only numbers or romeNumbers  or complex like 100000000000
# print(q.isupper())
# print(q.lower())
# print(q.istitle())
# print(q.isprintable()) #print the printable strings




#code generator
# import random 
# letter_a = "abdefghijklmnopqrstuvwxyz"
# letter_A = letter_a.upper()
# symbols = "!@#$%^&*()+=?\|"
# numbers = "1234567890"
# p = letter_A + letter_a + symbols + numbers

# passwords_count = int(input("write the count of your new password \n:"))
# letters_count = int(input("letters count ? \n:"))

# for i in range(passwords_count):
#     password = ""
#     for k in range(letters_count):
#         pletters = random.choice(p)
#         password += pletters
#     print(password)



# me = "python"
# print(me[-2])

# s = "javascript"
# # print(len(s))
# for i in range(len(s)):
#     print(s[i])

# arr = [12,32,4,12,32,12,312,13]
# arr.sort()
# print(arr[-2])


# i = 0
# while True:
#     i += 100
#     print(i)











# 1 - assignment
# user = int(input("k \n:"))
# far = int(input("n \n:"))
# for i in range(0,far):
#     print(user)

# 2 - assignment
# a = int(input("a \n:"))
# b = int(input("b \n:"))
# if a < b:
#     for j in range(a,b + 1):
#         print(j)

# 3 - assignment
# a = int(input("a \n:"))
# b = int(input("b \n:"))
# if a < b:
#     for j in range(a + 1, b): 
#         print(j)


# 4 - assignment
# user = int(input("price for per kg ?"))
# for i in range(1,11):
#     print(i * user)

# 5 - assignment
# user = int(input("price for per kg ?"))
# for i in range(10):
#     res = i / 10 * 1
#     res2 = res * user
#     print(int(res2))

# 6 - assignment
# def task(): 
#     user = int(input("price for per kg ?"))
#     for i in range(10):
#         res = i / 10 * 2
#         res2 = res + user 
#         print(int(res))
# task()

# 7 - assignment
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a , b):
#     print(i)

# 8 - assignment
# summa = 1 
# for i in range(1,11):
#     summa *= i
# print(summa)

# 9 - assignment
# a = 1
# b = 5
# for i in range(a,b+1):
#     kv = i ** 2
#     print(kv)

# 10 - assignment
# 11 - assignment
# 12 - assignment
# 13 - assignment
# 14 - assignment

# 15 - assignment
# a = 5
# n = int(input("n = "))
# mlt = a ** n
# print(mlt)

# 16 -assignment
# a = 2
# n = int(input("n = "))
# for i in range(1,n + 1):
#     print(i)

 

# narx = 15000 #mijoz 15 somga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False

# if choy:
#     print("choy oldi")
#     narx = narx + 3000
# if salat:
#     print("salat oldi")
#     narx = narx + 5000
# if non:
#     print("non oldi")
#     narx = narx + 2000
# if kompot:
#     print("kompot oldi")
#     narx = narx + 5000
# if assorti:
#     print("assorti oldi")
#     narx = narx + 15000

# print(f"Jami {narx} so`m")



# in operatori
# menu = ['pilav' , 'kebab' , 'narin' , 'samsa']
# order = input('what do you want to consume?')
# if order.lower() in menu:
#     print("ok, we are coming")
# else:
#     print("\nwe do not have that kind of meal, sorry") 


# menu = ['pilav' , 'kebab' , 'narin' , 'samsa']
# order = ['kebab' , 'lagman' , 'narin']
# for meal in order:
#     if meal.lower() in menu:
#         print(f"yeah, we have {meal}")
#     else:
#         print(f"sorry, we do not have {meal}") 

# list1 = [1,2,3]
# if len(list1) > 0:
#     print(True)
# else:
#     print(False)
# list2 = []
# if len(list2) > 0:
#     print(True)
# else:
#     print(False)




