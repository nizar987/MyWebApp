from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Experience, Contact, About
from .forms import ContactForm

# Create your views here.

def home(request):
    """Home page view"""
    projects = Project.objects.all()[:6]  # Show latest 6 projects
    skills = Skill.objects.all()
    experiences = Experience.objects.all()[:3]  # Show latest 3 experiences
    about = About.objects.first()
    
    context = {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'about': about,
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page view"""
    about_info = About.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    
    context = {
        'about': about_info,
        'skills': skills,
        'experiences': experiences,
    }
    return render(request, 'main/about.html', context)

def projects(request):
    """Projects page view"""
    projects = Project.objects.all()
    
    context = {
        'projects': projects,
    }
    return render(request, 'main/projects.html', context)

def project_detail(request, pk):
    """Individual project detail view"""
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found.')
        return redirect('projects')
    
    context = {
        'project': project,
    }
    return render(request, 'main/project_detail.html', context)

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send email notification (optional)
            try:
                send_mail(
                    f'New Contact Message: {contact.subject}',
                    f'From: {contact.name} ({contact.email})\n\nMessage:\n{contact.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL] if hasattr(settings, 'ADMIN_EMAIL') else [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except:
                pass  # Email sending is optional
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'main/contact.html', context)
