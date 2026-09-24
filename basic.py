user_name = input("Enter your name: ")
print("Hello, " + user_name + "! Welcome to RoadCo")

# multi = int(days) * 2

try:
    days = int(input("Enter the number of days you want to rent: "))
    rental_cost_per_day = 110
    total_cost = days * rental_cost_per_day
    print(f"The total cost of renting the car for {days} days is: ${total_cost}")
except ValueError:
    print("Please enter a whole number of days.")