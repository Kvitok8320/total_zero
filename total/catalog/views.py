from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def catalog_view(request):
    return render(request, "catalog/catalog.html")