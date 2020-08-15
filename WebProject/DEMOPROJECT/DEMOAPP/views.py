from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('<h1>This is My Homee ... </h1>')
    return render(request, 'DEMOAPP/index.html')

def events(request):
    return render(request, 'DEMOAPP/events.html')

def aboutClique(request):
    return render(request, 'DEMOAPP/about-us.html')

def interestship1(request):
    return render(request, 'DEMOAPP/interestship.html')

def informativeTalks(request):
    return render(request, 'DEMOAPP/talk.html')

def triviaEve(request):
    return render(request, 'DEMOAPP/trivia.html')

