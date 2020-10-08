from .models import Office_Address


def context_data(request):
    query = Office_Address.objects.all()
    return {'context_data': query, }
