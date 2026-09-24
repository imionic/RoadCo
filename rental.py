user_name = input("Enter your name: ")
print("Hello, " + user_name + "! Welcome to RoadCo")
car_type = " "
def car_choose():
    while True:
        car_type = input("Enter the type of car you want to rent Sedan, SUV: ").strip().lower()
        if car_type in ("sedan", "suv"):
            return car_type.upper() if car_type == "suv" else car_type.title()
        print("Please enter Sedan or SUV.")

choosen_car = car_choose()
print("Car Type: " + choosen_car)

def rental_days():
    while True:
        try:
            days = int(input("Enter the number of days you want to rent: "))
            if days <= 0:
                print("Please enter a valid number of days.")
                continue
            return days
        except ValueError:
            print("Please enter a whole number of days.")

req_days = rental_days()
print(f"Days Rented: {req_days}")

if choosen_car == "Sedan":
    rental_cost_per_day = 30
elif choosen_car == "SUV":
    rental_cost_per_day = 50

total_cost = req_days * rental_cost_per_day

if req_days > 7:
    discount = 10
    final_total_cost = total_cost * (1 - discount / 100)
    total_discount = total_cost - final_total_cost
    print(f"Discount Applied (10%): ${total_discount:.2f}")
else:
    discount = 0
    final_total_cost = total_cost
    print(f"No discount applied. Sub Total: ${final_total_cost}")

print(f"The total cost of renting the {choosen_car} for {req_days} days is: ${final_total_cost}")
