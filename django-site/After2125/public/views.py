from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.utils import timezone
from .models import After, Utilisateur, Ritz, Utilisateur_After




def index(request):
    # Filter After objects to include only those occurring today or later
    today = timezone.now()
    afters = After.objects.filter(jour__gte=today)

    # Organize parties by day of the week
    parties_by_day = {}
    for after in afters:
        day = after.jour.strftime('%A')  # Get day name (Monday, Tuesday, etc.)
        if day not in parties_by_day:
            parties_by_day[day] = []
        parties_by_day[day].append(after)

    # Pass the organized data to the template
    context = {'parties_by_day': parties_by_day}
    return render(request, 'index.html', context)

class MenusView(generic.ListView):
        model = Ritz
        context_object_name = 'Menus'
        queryset = Ritz.objects.all()
        template_name = 'Menus.html'
        
