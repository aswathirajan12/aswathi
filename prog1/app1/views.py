
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from.models import student
from.aswa import sample
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def display(request):
   if request.method=='GET':
       data=student.objects.all()
       s=sample(data,many=True)
       return JsonResponse(s.data,safe=False)

   elif request.method=='POST':
       d = JSONParser().parse(request)
       s=sample(data=d)
       if s.is_valid():
           s.save()
           return JsonResponse(s.data,safe=False)
       else:
           return JsonResponse(s.errors)

@csrf_exempt
def display2(request,r):
    try:
        d = student.objects.get(id=r)
    except Exception:
        return HttpResponse("does not exist")
    if request.method == 'GET':

        s = sample(d)
        return JsonResponse(s.data, safe=False)
    elif request.method == 'PUT':
        r = JSONParser().parse(request)
        s = sample(d,data=r)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data, safe=False)
        else:
            return JsonResponse(s.errors)
    elif request.method=="DELETE":
        d.delete()
        return HttpResponse("deleted")

# Create your views here.
