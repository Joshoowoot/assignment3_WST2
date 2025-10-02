from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Announcement
from .forms import AnnouncementForm

# Create your views here.
def home(request):
    context = {
        'title': 'Home Page', 
        'images': ['dancing_gekko.gif']
    }
    return render(request, 'home.html', context)

def announcements(request):
    announcements = Announcement.objects.filter(is_published=True)
    context = {
        'title': 'Announcements',
        'announcements': announcements
    }
    return render(request, 'announcements.html', context)

def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk, is_published=True)
    context = {
        'title': f'Announcement: {announcement.title}',
        'announcement': announcement
    }
    return render(request, 'announcement_detail.html', context)

def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Announcement created successfully!')
            return redirect('announcements')
    else:
        form = AnnouncementForm()
    
    context = {
        'title': 'Create Announcement',
        'form': form
    }
    return render(request, 'create_announcement.html', context)