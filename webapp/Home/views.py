from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'main.html')


def dataprocess(request):
    year = request.POST.get('year', False)
    transmission = request.POST.get('transmission', False)
    fuel = request.POST.get('fuel', False)
    city = request.POST.get('city', False)
    power = request.POST.get('power', False)
    engine = request.POST.get('engine', False)
    milage = request.POST.get('milage', False)
    seats = request.POST.get('seats', False)
    owner = request.POST.get('owner', False)
    tdistance = request.POST.get('tdistance', False)
    print(year)
    print(tdistance)
    data={
        "year":year,
        "transmission": transmission,
        "fuel": fuel,
        "city": city,
        "power": power,
        "engine": engine,
        "milage": milage,
        "seats": seats,
        "owner": owner,
        "tdistance": tdistance,
    }
    return render(request, 'display.html', {'data':data})

# Year 
# Enter the year
# Kilometers Driven 
# Enter the kilometers driven
# Owner type 
# Enter the owner type
# Seats 
# Enter the no. of seats
# Mileage(km/kg) 
# Enter the mileage
# Engine(CC) 
# Enter the engine
# Power(bhp) 
# Enter the power
# Location 
# Select Option
# Fuel-Type 
# Select Option
# Transmission
