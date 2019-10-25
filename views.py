from django.shortcuts import render

from django.http import HttpResponse
from .models import Tutorial
from .models import Destination
# Create your views here.

def homepage(request):
	return render(request=request,
				  template_name="main/header.html",
				  context={"tutorials": Tutorial.objects.all})


def add(request):
	val1 = int(request.GET["num1"])
	val2 = int(request.GET["num2"])
	res = val1 + val2


	return render(request,"main/result.html",{'result':res})


def travello(request):
	dest1 = Destination()
	dest1.name = 'Ahmedabad'
	dest1.desc = 'The first historical city of india'
	dest1.price = 786
	dest1.img = 'destination_7.jpg'

	dest2 = Destination()
	dest2.name = 'Surat'
	dest2.desc = 'The city of diamond'
	dest2.price = 745
	dest2.img = 'destination_4.jpg'

	dest3 = Destination()
	dest3.name = 'Mumbai'
	dest3.desc = 'The city of dreams'
	dest3.price = 900
	dest3.img = 'destination_4.jpg'


	dest = [dest1,dest2,dest3]

	return render(request=request,template_name="main/index.html",context={'dests': dest})