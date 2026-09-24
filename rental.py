user_name = input("Enter your name: ")
print("Hello, " + user_name + "! Welcome to RoadCo")

while True:
    car_type = input("Enter the type of car you want to rent Sedan, SUV: ").strip().lower()
    if car_type in ("sedan", "suv"):
        car_type = car_type.upper() if car_type == "suv" else car_type.title()
        break
    print("Please enter Sedan or SUV.")

print("Car Type: "+ car_type)

try:
    days = int(input("Enter the number of days you want to rent: "))
    rental_cost_per_day = 110
    total_cost = days * rental_cost_per_day
    discount = 10
    final_total_cost = total_cost * (1 - discount / 100)
    print(f"Discount Applied (10%): ${final_total_cost}")
    print(f"The total cost of renting the {car_type} for {days} days is: ${final_total_cost}")
except ValueError:
    print("Please enter a whole number of days.")
