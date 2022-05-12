from posixpath import abspath
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import pickle

from sklearn.feature_extraction import DictVectorizer


def home(request):
    return render(request, 'home.html')


def main(request):
    return render(request, 'main.html')

def dataprocess(request):
    name = request.POST.get('company', False)
    year = 2022-(int(request.POST.get('year', False)))
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
        r'D:\Study\VScode\KJ_SEM4\MP\Used-car-price-prediction\test.sav', 'rb')
    loaded_model = pickle.load(a)
    cityinput = "Location_"+city
    petrolinput = "Fuel_Type_"+fuel
    transinput = "Transmission_"+transmission
    nameinput = "Company_"+name
    ownerinput = "Owner_Type_"+owner
    dic = {'Year': year, 'Kilometers_Driven': tdistance, 'Seats': seats, 'Mileage(km/kg)': milage, 'Engine(CC)': engine,
           'Power(bhp)': power, 'Location_Bangalore': 0, 'Location_Chennai': 0,
           'Location_Coimbatore': 0, 'Location_Delhi': 0, 'Location_Hyderabad': 0,
           'Location_Jaipur': 0, 'Location_Kochi': 0, 'Location_Kolkata': 0,
           'Location_Mumbai': 0, 'Location_Pune': 0, 'Fuel_Type_Diesel': 0, 'Fuel_Type_LPG': 0,
           'Fuel_Type_Petrol': 0, 'Transmission_Manual': 0, 'Company_Audi': 0,
           'Company_Bmw': 0, 'Company_Bentley': 0, 'Company_Chevrolet': 0, 'Company_Datsun': 0,
           'Company_Fiat': 0, 'Company_Force': 0, 'Company_Ford': 0, 'Company_Honda': 0,
           'Company_Hyundai': 0, 'Company_Isuzu': 0, 'Company_Jaguar': 0, 'Company_Jeep': 0,
           'Company_Lamborghini': 0, 'Company_Land': 0, 'Company_Mahindra': 0,
           'Company_Maruti': 0, 'Company_Mercedes-Benz': 0, 'Company_Mini': 0,
           'Company_Mitsubishi': 0, 'Company_Nissan': 0, 'Company_Porsche': 0,
           'Company_Renault': 0, 'Company_Skoda': 0, 'Company_Tata': 0, 'Company_Toyota': 0,
           'Company_Volkswagen': 0, 'Company_Volvo': 0, 'Owner_Type_First': 0,
           'Owner_Type_Fourth & Above': 0, 'Owner_Type_Second': 0, 'Owner_Type_Third': 0
           }
    dic[f"{cityinput}"] = 1
    dic[f"{petrolinput}"] = 1
    dic[f"{nameinput}"] = 1
    dic[f"{ownerinput}"] = 1
    if transmission == "Manual":
        dic[f"{transinput}"] = 1
    userval = pd.DataFrame(dic, index=[0])
    y_pred = loaded_model.predict(userval)
    data = {
        "name": name,
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
        "result": str(round(y_pred[0], 2))
    }
    return render(request, 'display.html', {'data': data})
