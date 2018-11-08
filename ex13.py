def hotel_cost(nights):
    cost = 70
    return cost*nights

def plane_ticket_cost(city, klass):
    flight_cost = 0
    
    if city.lower == "new york":
        flight_cost = 2000
    elif city.lower == "auckland":
        flight_cost =  790
    elif city.lower == "venice":
        flight_cost =  154
    elif city.lower == "glasgow":
        flight_cost =  65
    return flight_cost*klass

def rental_car_cost(days):
    cost = days*30
    if days >= 7:
        cost -=50
    elif days >= 3:
        cost -=30
    return cost

def total_cost():
    cost = 0
    
   
    
    
    
    print("List of cities to travel: \n", "New York \n", "Auckland \n", "Venice \n", "Glasgow")
    city = str(input("Type the city to visit:"))
    print("Pick a class: \n", "Economy: 1 \n", "Premium Economy: 1.3 \n", "Business Class: 1.6 \n", "First Class: 1.9 \n", "Please enter the decimal value displayed... ")
    klass = float(input())
    cost += plane_ticket_cost(city, klass)
    print("Car Hire is £30 per day \n", "A £50 discount will be applied for rentals over 7 days \n", "A £30 discount will be applied for rentals between 3-6 days")
    print("Enter how many days you want to hire: ")
    days = int(input())
    cost += rental_car_cost(days)
    
    cost += hotel_cost(days-1)


    print("The final cost of your trip is", cost)

    
total_cost()

