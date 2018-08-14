from django.shortcuts import render
from django.http import HttpResponse
from funplace.controller import FunplaceController

# Create your views here.
funplaceController = FunplaceController()

def myView(request):
	context = {'name': 'Bob'}
	return render(request, 'funplace/fun.html', context)

def mySimpleView(request):
	return HttpResponse("Hello!")

def showFunPlaces(request):
	context = {'funplaces': funplaceController.getFunplaces()}
	return render(request, 'funplace/fun1.html', context)

def showFunPlaces2(request):
	context = {'funplaces': funplaceController.getFunplaces()}
	return render(request, 'funplace/fun2.html', context)

def addFunPlace(request):
	if request.method == 'GET':
		return render(request, 'funplace/add.html')
	elif request.method == 'POST':
		placeName = request.POST.get("placeName", None)
		country = request.POST.get("country", None)
		isSaved = funplaceController.savePlace(placeName, country)
		context = {"isPostResponse": True, "isSaved": isSaved}
		return render(request, 'funplace/add.html', context)
