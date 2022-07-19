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

def propietario(request):
    return render(request, 'propietario.html', {})