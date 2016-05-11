
cars = 100	# number of cars
space_in_a_car = 4.0	# number of seats in car
drivers = 30	# number of drivers
passengers = 90	# number of passengers
cars_not_driven = cars - drivers	# number of cars not being used
cars_driven = drivers	# number of cars in use
carpool_capacity = cars_driven * space_in_a_car	# number of spaces available for passengers
average_passengers_per_car = passengers / cars_driven # average number of passengers per car
#THIS REQUIRED PARENTHESES EVEN THOUGH THE INSTRUCTIONS DIDNT HAVE THEM
print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
