# Area of rectangle is length*breadth
# length =int(input("enter the length: "))
# breadth =int(input("enter the breadth: "))

# print(length*breadth)

# Area of Circle is pi*r*r 
# pi = 3.14
# r =float(input("the radius of circle is: "))
# print(pi*r*r)

# Net price on anything.
# m1 =int(input("Enter first subject number: "))
# m2 =int(input("Enter second subject number: "))
# m3 =int(input("Enter third subject number: "))
# total_marks = m1+m2+m3
# percente =(total_marks*100)/300
# print("total marks obtained: ",total_marks)
# print("percentage: ",percente)

# Decision statement
# age =int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote")
# else:
#     print("You can not vote")

# Greater & Less than.
# a =int(input("Enter A: "))
# b =int(input("Enter B: "))
# if a>b:
#     print("A is Greater")
# else: 
#     print("B is greater")

# Odd & Evev number check.
# num =int(input("Enter any number: "))
# if num%2 == 0:
#     print(f'{num} is Even number')
# else:
#     print(f'{num} is Odd number')

# Use Decision making and,or,and not.
# # Example=
# if a>b:
#     print("A")
# elif a<b:
#     print("B")
# else:
#     print("same")

# # like example=
# username = input("Enter Username: ")
# password = input("Enter Password: ")
# if username == 'patidarshubham900'and password == 'shubham':
#     print("Welcome Shubham.")
# elif username != 'patidarshubham900' and password == 'shubham':
#     print('username is invalid.')
# elif username == 'patidarshubham900' and password != 'shubham':
#     print('password are invalid.')
# else:
#     print("username and password both are incorret.")

# Hindi = int(input("Number of Hindi: "))
# English = int(input("Number of English: "))
# Maths = int(input("Number of Maths: "))
# Physics = int(input("Number of Physics: "))
# Chemistry = int(input("Number of Chemistry: "))
# total_marks = Hindi+English+Maths+Physics+Chemistry
# percente =(total_marks*100)/500
# print("total marks obtained: ",total_marks)
# print("percentage: ",percente)
# if Hindi<33:
#     print("Supply in Hindi")
# if English<33:
#     print("Supply in English")
# if Maths<33:
#     print("Supply in Maths")
# if Physics<33:
#     print("Supply in Physics")
# elif Chemistry<33:
#     print("Supply in Chemistry")
# elif percente >= 80:
#     print("Pass with grade A.")
# elif percente >= 60:
#     print("Pass with grade B")
# elif percente >= 33:
#     print("Pass with grade C")
# else:
#     print("Fail")

# # Example of price quantity and discount.
# Price =float(input("Enter the price: "))
# Qty =float(input("Enter the Qty: "))
# net_price = Price*Qty
# # dis =(net_price*10)/100
# # amount = net_price-dis
# # print(amount)

# # We applying a conditions.
# if net_price<1000:
#     dis = (net_price*10)/100
# elif net_price>=1000 and net_price<2000:
#     dis = (net_price*20)/100
# elif net_price>=2000:
#     dis = (net_price*30)/100
# amount = net_price-dis
# print(amount)

# # Example character check.
# ch =input("enter any character: ")
# if ch =="a" or ch =="e" or ch =="i" or ch =="o" or ch =="u":
#     print("It is vowels.")
# else:
#     print("It is not vowels.")

# Loops in python. Two types of loop (1)for loop (2)while loop.
# Examples.

# for i in range(1,6):
#     print("Welcome to python programming.")

# for i in range(10,1,-1):
#     print("i")

# Range() can be move positive like range(1,10) or negative like range(10,1,-1) and also can be used with step like range(1,10,2) or range(10,1,-2).

# Example of sum.
# sum = 0
# for i in range(1,11):
#     sum = sum+i
# print(f'Sum of series is {sum}')

# n = int(input("Enter limit: "))
# for i in range(1,n+1):
#     print("i")

# Table generation with the help of loop.
# n = int(input("Enter any number: "))
# for i in range(1,11):
#     t = n*i
#     print(t)

# Example of Factorial.
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(n,0,-1):
#     fact = fact*i
# print(fact)

# Using and Examples of While Loop.

# i = 1 
# while i<=10:
#     print(i)
#     i = i+1,2,3
# print("loop ended")

# Program to reverse to given number.       (IMP)
# n = int(input("Enter any number: "))
# t = 0 
# while n>0:
#     r = n%10
#     t = t*10+r
#     n = n//10
# print(t)

# for i in range(1,11):
#     print(i,end=" ")
#     if i>=8:
#         break
#     print("Loop is breaked")
# print("Loop is ended")
# print("Bye")

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# for i in range(1,rows+1):
#     for j in range(1,cols+1):
#         print("*",end=" ")
#     print()

# Q. Count the total number of digits in a given number. (IMP)
# num = int(input("Enter any number: "))
# count = 0
# while num>0:
#     num = num//10
#     count = count+1
# print("total digit =",count)

# Nested Loop.  (IMP)
# Loop within another loop is called Nested loop.

# for i in range(1,13):
#     for j in range(1,13):
#         print("*",end=" ")
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# for i in range(1,8):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(6,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# for i in range(6,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

for i in range(1,6):
    for j in range(1,(10-i)+1):
        print("*",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
print()
    