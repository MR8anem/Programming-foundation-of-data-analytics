# 7.	Calculate the number of trays, N, needed to hold X glasses if each tray contains Y glasses.
import math

X = input("Enter number of Glasses : ")
Y = input("How Many glasses Tray can hold : ")
print("Number of trays is equal {}".format(math.ceil(int(X) / int(Y))))


# 8. If you distribute N apples in groups of 7 apples each, how many groups will contain exactly 7 apples and how many apples remain?

N = input("Enter Number of Apples to Group ")
print("Number of groups equal {}".format(int(N) // 7))
print("Number of Remaining Apples equal {}".format(int(N) % 7))



# 12.	Write a program that asks the user for three one-digit numbers and then uses them as units, tens, and hundreds to evaluate one 3-digit number out of them
# Example:
# Please enter units: 5
# Please enter tens: 2
# Please enter hundreds: 9
# The number is: 925


units = input(" Please enter units:")
tens  = input(" Please enter tens:")
hundreds = input(" Please enter hundreds:")
print("The number is: {}".format(hundreds+tens+units))


