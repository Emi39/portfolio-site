from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project, Profile
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    featured_projects = Project.objects.filter(is_featured=True).order_by('-created_at')[:6]
    return render(request, 'home.html', {
        'profile': profile,
        'projects': featured_projects
    })

def portfolio_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def about(request):
    profile = Profile.objects.first()
    return render(request, 'about.html', {'profile': profile})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    profile = Profile.objects.first()
    return render(request, 'contact.html', {'form': form, 'profile': profile})
