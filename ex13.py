def hotel_cost(nights):
    cost = 70
    return cost*nights

def plane_ticket_cost(city, klass):
    if city.lower == "new york":
        return 2000
    elif city.lower == "auckland":
        return 790
    elif city.lower == "venice":
        return 154
    elif city.lower == "glasgow":
        return 65
    return city + city*klass

def rental_car_cost(days):
    cost = days*30
    if days >= 7:
        cost -=50
    elif days >= 3:
        cost -=30
    return cost

def total_cost(city, days):
    cost = 0
    cost += hotel_cost
    cost += plane_ticket_cost

    print("List of cities to travel: \n", "New York \n", "Auckland \n", "Venice \n", "Glasgow")
    print("Pick a class: \n", "Economy: 1 \n", "Premium Economy: 1.3 \n", "Business Class: 1.6 \n", "First Class: 1.9 \n", "Please enter the decimal value displayed... ")

    cost += city + city*klass

    print("Car Hire is £30 per day \n", "A £50 discount will be applied for rentals over 7 days \n", "A £30 discount will be applied for 3-6 days")
    print("Enter how many days you want to hire: ")

    cost += rental_car_cost
    
    print("The final cost of your trip is", cost)

days = int(input())
klass = float(input())
city = str(input())
total_cost(city,days)

