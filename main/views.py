from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406439192',
        'name': 'Anak Agung Ngurah Abhivadya Nandana',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
