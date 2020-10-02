from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')
def law_firm_view(request):
    return render(request,'Law_firm.html')
def practice_view(request):
    return render(request,'Practices.html')
def attorneys_view(request):
    return render(request,'Attorneys.html')
def offices_view(request):
    return render(request, 'Offices.html')
def disclaimer_view(request):
    return render(request, 'disclaimer.html')
def sitemap_view(request):
    return render(request, 'sitemap.html')
def blog_view(request):
    return render(request, 'blog.html')
def inside_practice_view(request):
    return render(request, 'inside_practice.html')
