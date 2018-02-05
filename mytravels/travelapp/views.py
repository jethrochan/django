from django.shortcuts import render
from . models import *

def index(request):
    Reports = Report.objects.all()
    return render(request, 'travelapp/index.html', 
    {
        'Reports':Reports,
    })
    
def destination(request, pk):
    destinationReport =  Report.objects.get(pk = pk)
    return render(request, 'travelapp/destination.html', 
    {
        'report':destinationReport,
    })
