from django.shortcuts import render


def home(request):
    context = {
        'title': 'StartGreat',
        'heder_title': "La productivité et l'efficacité ",
    }
    print(request.headers)
    return render(request, 'personal/home.html', context)