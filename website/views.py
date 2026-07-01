from django.shortcuts import render

def home(request):
    return render(request, "index.html")


def booking(request):

    return render(request, "booking.html")