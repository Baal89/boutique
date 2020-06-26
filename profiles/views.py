from django.shortcuts import render

# Create your views here.

def profile(request):
    """ display user's profile"""

    template = 'profile/profile.html'
    context = {}

    return render(request, template, context)
