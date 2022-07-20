from django.shortcuts import render

from django.views.generic import View

from .models import Propietario, Motocicleta, Oficina, Prueba

from django.http import JsonResponse

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt

import json

class Propietarios(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, propietario_id=0):
        if (propietario_id > 0):
            propietario=list(Propietario.objects.filter(cedula=propietario_id).values())
            if len(propietario) > 0:
                resultado= propietario[0]
                data = {'propietario': resultado}
            else:
                data = {'msg': 'vacio'}
            return JsonResponse(data)
        else:
            propietario = list(Propietario.objects.values())
            if len(propietario) > 0:
                data = {'lista_propietarios': propietario}
            else:
                data = {'message': 'vacio'}

            return JsonResponse(data)

    def post(self,request):
        jd = json.loads(request.body)
        Propietario.objects.create(cedula=jd['cedula'], nombre=jd['nombre'], s_nombre=jd['s_nombre'], apellido=jd['apellido'],
                    s_apellido=jd['s_apellido'], f_nacimiento=jd['f_nacimiento'], contra=jd['contra'])
        return JsonResponse(jd)

    def put(self,request, propietario_id):
        jd = json.loads(request.body)
        persons = list(Propietario.objects.filter(cedula=propietario_id).values())
        if len(persons) > 0:
            person = Propietario.objects.get(cedula=propietario_id)
            person.nombre = jd['nombre']
            person.s_nombre = jd['s_nombre']
            person.apellido = jd['apellido']
            person.s_apellido = jd['s_apellido']
            person.f_nacimiento = jd['f_nacimiento']
            person.contra = jd['contra']
            person.save()
            data = {'msg': 'datos atualizados'}
        else:
            data = {'msg': 'no econtrado'}
        return JsonResponse(data)

    def delete(self,request, propietario_id):
        persons = list(Propietario.objects.filter(cedula=propietario_id).values())
        if len(persons) > 0:
            Propietario.objects.filter(cedula=propietario_id).delete()
            data = {'msg':'deleted'}
        else:
            data = {'msg': 'not deleted'}
        return JsonResponse(data)


class Motocicletas(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, motocicleta_id=0):
        if (motocicleta_id > 0):
            motos=list(Motocicleta.objects.filter(propietario_cedula=motocicleta_id).values())
            if len(motos) > 0:

                moto= motos[0]
                data = {'moto': moto}
            else:
                data = {'msg': 'vacio'}
            return JsonResponse(data)
        else:
            motos = list(Motocicleta.objects.values())
            if len(motos) > 0:
                data = {'listado_motos': motos}
            else:
                data = {'message': 'vacio'}

            return JsonResponse(data)

class Pruebas(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, prueba_id=0):
        if (prueba_id > 0):
            pruebas=list(Prueba.objects.filter(idprueba=prueba_id).values())
            if len(pruebas) > 0:
                prueba= pruebas[0]
                data = {'prueba': prueba}
            else:
                data = {'msg': 'vacio'}
            return JsonResponse(data)
        else:
            pruebas = list(Prueba.objects.values())
            if len(pruebas) > 0:
                data = {'listado_pruebas': pruebas}
            else:
                data = {'message': 'vacio'}

            return JsonResponse(data)


    
class Oficinas(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, oficina_id=0):
        if (oficina_id > 0):
            oficinas=list(Oficina.objects.filter(idOficina=oficina_id).values())
            if len(pficinas) > 0:
                oficina= oficinas[0]
                data = {'oficina': oficina}
            else:
                data = {'msg': 'vacio'}
            return JsonResponse(data)
        else:
            oficinas = list(Oficina.objects.values())
            if len(oficinas) > 0:
                data = {'listado_oficinas': oficinas}
            else:
                data = {'message': 'vacio'}

            return JsonResponse(data)


