# 2.	Write a program that reads the user full name and prints first name and last name separately.
# Example1:
# Enter name: Mohamed Ahmed
# Your first name is: Mohamed
# Your last name is: Ahmed
#
# Example2:
# Enter name: Mohamed Ahmed Kamal
# Your first name is: Mohamed
# Your last name is: Kamal

Name = input("Please Enter your Name").split()
print("Your first name is {}".format(Name[0]))
print("Your Last name is {}".format(Name[len(Name)-1]))


# 3.Write a program that reads a statement form the user and counts the number of vowel letters in the statement. If no vowels found the program prints “No vowels found”.

statement = list(input("please enter statement"))
vowels = ['a' ,'e' ,'i' ,'o' ,'u']
count = 0
for vowel in vowels :
    for letter in statement:
        if letter == vowel:
            count += 1
if count != 0:
    print("Numbers of vowels in statement is",count)
else:
    print("No vowels found")



# 5.Write a program to read a list of students’ grades from the user and do the following:
grades = input("Enter student grades please : ").split()
# a.Check each element if it is a valid grade (valid range is from 0 to 100). For each grade, the program displays either Valid or Invalid. Count number of invalid grades.
count = 0
binarylist = []
sum =0
for grade in grades :
    if int(grade)  in range(0,101):
        print("valid")
        binarylist.append(1)
        sum += int(grade)
        lowest = int(grades[0])
        largest = int(grades[0])
        if int(grade) < lowest:
            lowest = int(grade)
        else:
            largest = int(grade)
    else:
        count += 1
        print("Invalid")
        binarylist.append(0)
print("print number of grades is ",len(grades)-count, "and number of invalid grades is", count )




# b.Check each element if it is a valid grade (valid range is from 0 to 100). Produce a corresponding list (same size as the grades list) that has 1 or 0 in the same grade position; 1 if the grade is valid and 0 if it is invalid.

print(binarylist)
# c.	Calculate and display the average grade.
avarage =sum / len(grades)
print("average equal {}".format(sum / len(grades)))
# d.	Find and display the highest and lowest grades and specify their locations.
print("highest grade is ",largest,"and lowest grade is ", lowest)

# e.	Allocate and display students having grades greater than 85%, and display their count.
counter = 0
for i in range(len(grades)):
    if grades[i] in range(86, 100):
        counter +=1
        print("student {} have grade greater than 85% ".format(i))
        print("number of students have grades greater than 85% is {}".format(counter))
# f.	Allocate and display students having grades greater than average, and display their count.
counter = 0
for i in range(len(grades)):
    if int(grades[i]) in range(0,101):
        if int(grades[i]) > avarage:
            counter +=1
print("student {} have grade greater than avarage ".format(i))
print("number of students have grades greater than avarage is {}".format(counter))

#-1 20 30 40 100 1010 2134