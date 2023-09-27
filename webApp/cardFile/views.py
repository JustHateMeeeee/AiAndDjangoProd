from django.shortcuts import render

def videoCards(request):
    return render(request, 'cardFile/videoCards.html')

def mainList(request):
    return render(request, 'cardFile/mainList.html')

def ssdHdd(request):
    return render(request, 'cardFile/ssdHdd.html')


def ram(request):
    return render(request, 'cardFile/ram.html')

def core(request):
    return render(request, 'cardFile/core.html')

def power(request):
    return render(request, 'cardFile/power.html')

def cooler(request):
    return render(request, 'cardFile/cooler.html')