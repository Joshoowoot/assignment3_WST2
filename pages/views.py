from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Home Page', 'features': ['Django', 'Templates', 'Static Files']
    }
    return render(request, 'home.html', context)

def announcements(request):
    context = {
        'title': 'Announcements Page'
    }
    return render(request, 'announcements.html', context)