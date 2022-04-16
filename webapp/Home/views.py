from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'main.html')


def dataprocess(request):
    year = request.GET.get('year', False)
    # if (year == False) or (year == ""):
    #     return render(request, 'main.html')
    print(year)
    data={
        "year":year
    }
    return render(request, 'display.html', {'data':data})
# Enter car details
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
