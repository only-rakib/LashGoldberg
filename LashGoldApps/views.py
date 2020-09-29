from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')
def law_firm_view(request):
    return render(request,'Law_firm.html')
def practice_view(request):
    return render(request,'Practices.html')
