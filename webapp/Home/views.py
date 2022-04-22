import pathlib
from posixpath import abspath
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import pickle

from sklearn.feature_extraction import DictVectorizer


def home(request):
    return render(request, 'main.html')


def dataprocess(request):
    year = int(request.POST.get('year', False))
    transmission = request.POST.get('transmission', False)
    fuel = request.POST.get('fuel', False)
    city = request.POST.get('city', False)
    power = float(request.POST.get('power', False))
    engine = float(request.POST.get('engine', False))
    milage = float(request.POST.get('milage', False))
    seats = float(request.POST.get('seats', False))
    owner = request.POST.get('owner', False)
    tdistance = int(request.POST.get('tdistance', False))

    a = open(
        r'D:\Study\VScode\KJ_SEM4\MP\Used-car-price-prediction\webapp\Home\test.sav', 'rb')
    loaded_model = pickle.load(a)
    cityinput = "Location_"+city
    petrolinput = "Fuel_Type_"+fuel
    transinput = "Transmisson_"+transmission
    dic = {'Year': 0, 'Kilometers_Driven': 0, 'Owner_Type': 0, 'Seats': 0.0,
           'Mileage(km/kg)': 0.0, 'Engine(CC)': 0.0, 'Power(bhp)': 0.0,
           'Location_Bangalore': 0, 'Location_Chennai': 0, 'Location_Coimbatore': 0,
           'Location_Delhi': 0,
           'Location_Hyderabad': 0, 'Location_Jaipur': 0,
           'Location_Kochi': 0, 'Location_Kolkata': 0, 'Location_Mumbai': 0,
           'Location_Pune': 0, 'Fuel_Type_Diesel': 0, 'Fuel_Type_LPG': 0,
           'Fuel_Type_Petrol': 0, 'Transmission_Manual': 0,
           }
    dic[f"{cityinput}"] = 1
    dic[f"{petrolinput}"] = 1
    if transmission == "Manual":
        dic[f"{transinput}"] = 1
    userval = pd.DataFrame(dic, index=[0])
    y_pred = loaded_model.predict(userval)
    print(y_pred[0])
    data = {
        "year": year,
        "transmission": transmission,
        "fuel": fuel,
        "city": city,
        "power": power,
        "engine": engine,
        "milage": milage,
        "seats": seats,
        "owner": owner,
        "tdistance": tdistance,
        "result": y_pred
    }
    return render(request, 'display.html', {'data': data})

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
