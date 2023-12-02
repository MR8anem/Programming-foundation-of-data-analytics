import math

# Question 1 
# while True : 
#     brings = input("what did team members bring?").split()
#     if "battery"  in brings : 
#         print("I donot need to bring the battery")   
#     else:
#         print("I will need to bring the battery")

# Question 2
#2.	Write a program to read three numbers from the user and print them in ascending order.

# numbers = input("Enter 3 numbers to sort").split()
# print(int(sorted(numbers)))

# Another way to solve 
# store = 0
# for i in range(0 , (len(numbers) -1 )) : 
#     for j in range(1, len(numbers)):
#         if  int(numbers[i])> int(numbers[j]) : 
#             store = numbers[i]
#             numbers[i] = numbers[j]
#             numbers[j] = store
# print(numbers)

# Question 3

# soup = input("Please Enter Your Soup")
# meal = input("Please Enter Your Meal")
# if soup == "mushroom"and meal == "mashed potatoes":
#     print("she loves vegetables")
# elif soup == "sea food" and meal == "grilled chicken":
#     print("she hates vegetables")
# else:
#     print("she neither hate nor love vegetables")


# Question 4
# E = "y"
# while E == "y":
#     for i in range(5):
#         weight = int(input("Enter weight \n>> "))
#         if weight <= 0 : 
#             print("invalid weight")
#             continue
#         unit = input("● 1 for mg \n● 2 for Kg\n● 3 for ton\n>> ")
        
#         if unit == "1" :
#             print("{} mg equal {} Gram".format(weight , (weight / 1000)))
#         elif unit == "2" : 
#             print("{} Kg equal {} Gram".format(weight , (weight * 1000)))
#         elif unit == "3" :
#             print("{} Ton equal {} Gram".format(weight , (weight * 1000*1000)))
#         else :
#             print("invalid unit")
#     E = input("if you need to continue press y : ").lower()



# Question 6

# a = float(input("Enter a \n>> "))
# b = float(input("Enter b \n>> "))
# c = float(input("Enter c \n>> "))

# if a == b == c == 0 : 
#     print("Any x is a solution")
# elif a == b == 0 and c != 0 :
#     print("No solution")
# elif a == 0 :
#     print("one real root equal {}".format((-c / b)))
# else : 
#     root1 = (-b + math.sqrt((b**2)- 4*a*c))/2*a
#     root2 = (-b - math.sqrt((b**2)- 4*a*c))/2*a
#     print("two real or complex roots are {} and {} ".format(root1 , root2))


# Quesion7 

friends  = input("enter friends\n>> ").split()
presents = input("enter presents\n>> ").split()
mind_gift = input("what is in his mind ? \n>> ")
if mind_gift in presents : 
    index = presents.index(mind_gift)
    print("Oh {}, Thank you friend :)".format(friends[index]))
else : 
    print("Opps, Sorry none")