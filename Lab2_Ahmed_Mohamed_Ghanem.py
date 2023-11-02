# 4.	Write a program to get a number N from the user, and check if it is negative: a message should be displayed to say that the number is negative. Otherwise: it should print the summation of the numbers from 1 to N.

N = int(input("Enter Number to Check :"))
if N < 0 :
    print("the number is negative")
else:
    # i can use simple algorithm ((N * N+1) / 2) --> but i try to use for loops
    sum = 0
    for i in range(N+1):
        sum += i
    print("The number is sum from 1 to N is Equal : {}".format(sum))

# 6.	Write a program to read N numbers from the user and prints the sum of the odd elements and the sum of the even elements.

Num = input("Enter Number in form of --> Num1 Num2 Num3 \n").split()
even = 0
odd = 0
for i in Num :
    if int(i) % 2 == 0 :
        even += int(i)
    else:
        odd += int(i)
print("sum of even is {} & sum of odd is {}".format(even,odd))

# 9.Write a program that reads the departure time of a train and the arrival time and computes and displays the trip time. (Example: for Departure time 10:50 and Arrival time 12:10 the trip time will be 1 hr and 20 min)

Departure = input("Enter Departure time in formate hh:mm ").split(':')
Arrival = input("Enter Arrival time in formate hh:mm ").split(':')

MinutesDeparture = (int(Departure[0])*60) + int(Departure[1])
MinutesArrival = (int(Arrival[0])*60) + int(Arrival[1])
hours = ((MinutesArrival - MinutesDeparture) // 60)
minutes = ((MinutesArrival - MinutesDeparture) % 60)
print("time of trip is {} hours and {} minutes".format(hours , minutes))
