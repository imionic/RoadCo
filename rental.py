user_name = input("Enter your name: ")
print("Hello, " + user_name + "! Welcome to RoadCo")

while True:
    car_type = input("Enter the type of car you want to rent Sedan, SUV: ").strip().lower()
    if car_type in ("sedan", "suv"):
        car_type = car_type.upper() if car_type == "suv" else car_type.title()
        break
    print("Please enter Sedan or SUV.")

print("Car Type: " + car_type)

while True:
    try:
        days = int(input("Enter the number of days you want to rent: "))
        print(f"Days rented: {days}")
        if days <= 0:
            print("Please enter a valid number of days.")
            continue
        break
    except ValueError:
        print("Please enter a whole number of days.")

if car_type == "Sedan":
    rental_cost_per_day = 30
elif car_type == "SUV":
    rental_cost_per_day = 50

total_cost = days * rental_cost_per_day

if days > 7:
    discount = 10
    final_total_cost = total_cost * (1 - discount / 100)
    total_discount = total_cost - final_total_cost
    print(f"Discount Applied (10%): ${total_discount:.2f}")
else:
    discount = 0
    final_total_cost = total_cost
    print(f"No discount applied. Sub Total: ${final_total_cost}")

print(f"The total cost of renting the {car_type} for {days} days is: ${final_total_cost}")
