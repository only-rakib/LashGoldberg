from django.shortcuts import render
from . models import Office_Address,PracticeArea

def home_view(request):
    return render(request, 'home.html')

def law_firm_view(request):
    return render(request,'Law_firm.html')

def practice_view(request):
    query_practice_area = PracticeArea.objects.all()
    return render(request, 'Practices.html', {'data': query_practice_area})


def practice_inside_view(request,slug):
    query = PracticeArea.objects.get(slug=slug)
    query_practice_area = PracticeArea.objects.all()
    return render(request,'inside_practice.html',{'data':query,'practice_area':query_practice_area})

def attorneys_view(request):
    return render(request,'Attorneys.html')

def offices_view(request):
    query_office = Office_Address.objects.all()
    return render(request, 'Offices.html', {'data': query_office})


def offices_inside_view(request, pk, office_title):
    query = Office_Address.objects.get(pk=pk)
    return render(request, 'offices_inside.html', {'offices': query})

def disclaimer_view(request):
    return render(request, 'disclaimer.html')

def sitemap_view(request):
    return render(request, 'sitemap.html')

def blog_view(request):
    return render(request, 'blog.html')

def inside_practice_view(request):
    return render(request, 'inside_practice.html')

def inside_our_team_view(request):
    return render(request, 'inside_our_team.html')
