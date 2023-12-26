#Q1
b

#Q2
TRUE

#Q3
10


#Q4
C=3

#Q5
a

#Q6
b & d

#Q7
b & e

#Q8
1 - 2 


#Q9 
Rows = int(input("Enter the number of rows :"))

for row in range(0,Rows):
    for column in range(row+1):
        print(f"{(column+1)**2}",end="\t")
    print("\n")



#Q10

epartments = ["Meat", "Seafood", "Milk", "Bread", "Oil"]
available_items = []
prices = []
promo_code = "123456"
cart = {department: 0 for department in departments}
report = {department: 0 for department in departments}
total_sold = 0

for department in departments:
    available = int(input(f"How many available items in {department}? "))
    available_items.append(available)
    price = float(input(f"What are the prices of the available items in {department}? "))
    prices.append(price)

while True:
    customer_cart = {department: 0 for department in departments}
    for i, department in enumerate(departments):
        quantity = int(input(f"How many you want from {department}? "))
        if quantity > available_items[i]:
            print(f"We are sorry, there's no available {department}.")
            continue
        customer_cart[department] = quantity
        available_items[i] -= quantity
        total_sold += quantity

    promo = input("Please enter promo if you have: ")
    if promo == promo_code:
        customer_cart["Milk"] = 0.7 * customer_cart["Milk"]  # Apply 30% discount on Milk

    total_price = sum(prices[i] * customer_cart[departments[i]] for i in range(len(departments)))
    print(f"Dear prospective customer, the total is: {total_price:.1f} pounds")

    store_open = input("Is the store still open? (yes/no) ")
    if store_open.lower() != "yes":
        break

    for department in customer_cart:
        cart[department] += customer_cart[department]

for department in report:
    report[department] = cart[department] / total_sold * 100
sorted_report = dict(sorted(report.items(), key=lambda item: item[1]))
print("We sold today:")
for department, ratio in sorted_report.items():
    print(f"{ratio:.2f}% {department}")
