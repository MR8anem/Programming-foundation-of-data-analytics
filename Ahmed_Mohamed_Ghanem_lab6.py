# Q1
#Qa --> a
#Qb --> c
#QC --> c


# Q2
#output --> 998 - 999 - 1000 -1001

#Q3
# 3.863   - 3.86 -     3.9  - 4 -3

#Q4
print("My name is Ahmed \n Friends call me \"Ghanem :)\ "\n\I don't like bananas&peaches")

#Q5

['Hello.', 'My', 'name', 'is', 'ahmed.', 'I', 'am', 'from', 'Cairo']
['Hello. My name is ahmed. I am from Cairo']
['Hello', ' My name is ahmed', ' I am from Cairo']
['Hello', 'My name is ahmed', 'I am from Cairo']


#Q6

lengths = [int(x) for x in input("Enter rectangle lengths ").split()]
widths = [int(x) for x in input("Enter rectangle widths ").split()]

print("Number\tlength\twidth\tArea(approximate)")

for i in range(len(lengths)):
    print("%d\t%0.2f\t%0.2f\t%.0f"%((i+1),lengths[i],widths[i],(lengths[i]*widths[i])))