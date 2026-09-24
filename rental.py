available_cars = {"sedan": 30, "suv": 50, "truck": 70, "van": 40, "sports car": 100}

def car_choose():
    while True:
        print("Available Transports are Sedan, SUV, Truck, Van, Sports Car.")
        car_type = input("Enter the type of car you want to rent: ").strip().lower()
        
        if car_type in available_cars:
            return car_type
        
        print("Please choose a valid car type from the available options.")


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

user_name = input("Enter your name: ")
print("Hello, " + user_name + "! Welcome to RoadCo")

choosen_car = car_choose()
print("Car Type: " + choosen_car.title())

req_days = rental_days()
print(f"Days Rented: {req_days}")

rental_cost_per_day = available_cars[choosen_car]
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

print(f"The total cost of renting the {choosen_car.title()} for {req_days} days is: ${final_total_cost}")
