from django.views.generic import View

from django.http import HttpResponse

from django.shortcuts import render, redirect

#from web_app.models import Person, Patient, Doctor, DoctorAcount, VitalSigns

from django.http import JsonResponse

#from w_page.forms import Patient_form, Doctor_form

import requests, json


def home(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

def succes(request):
    return render(request, 'succes.html', {})

#def succes_id(request,id):
#    return render(request, 'succes.html', {})

def propietario(request):
    return render(request, 'propietario.html', {})

def actualizar_id(request,id):
    # pull data from third party rest api
    # id = request.GET.get('id')
    response = requests.get('http://localhost:8000/api/propietario/' + str(id))

    # convert reponse data into json
    prop = response.json()

    # all_data = json.loads(users)

    context = {
        'data': prop,
    }
    # print(users)
    return render(request, 'actualizar.html', context)

def propietario_id(request,id):
    # pull data from third party rest api
    # id = request.GET.get('id')
    response = requests.get('http://localhost:8000/api/propietario/' + str(id))
    response2 = requests.get('http://localhost:8000/api/motocicleta/' + str(id))
    response3 = requests.get('http://localhost:8000/api/prueba/' + str(id))


    # convert reponse data into json
    prop = response.json()

    motos = response2.json()

    prueba = response3.json()


    # all_data = json.loads(users)

    context = {
        'data': prop,
        'motos': motos,
        'prueba': prueba,
    }
    # print(users)
    return render(request, 'propietario.html', context)


def succes_id(request, id):
    # pull data from third party rest api
    # id = request.GET.get('id')
    response = requests.get('http://localhost:8000/api/propietario/'+str(id))

    # convert reponse data into json
    prop = response.json()

    # all_data = json.loads(users)

    context = {
        'data': prop,
    }
    # print(users)
    return render(request, 'succes.html', context)
