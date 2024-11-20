from django.shortcuts import render

from django.http import JsonResponse
from django.utils import timezone
from shared.models import After, Utilisateur, Ritz, Utilisateur_After




def index(request):
    # Filter After objects to include only those occurring today or later
    today = timezone.now()
    afters = After.objects.filter(jour__gte=today).values('jour', 'participants__pseudo', 'ritz__plat')

    # Organize parties by day of the week
    parties_by_day = {}
    for after in afters:
        day = after['jour'].strftime('%A')  # Get day name (Monday, Tuesday, etc.)
        if day not in parties_by_day:
            parties_by_day[day] = []
        parties_by_day[day].append(after)

    # Pass the organized data to the template
    return JsonResponse({'parties_by_day': parties_by_day}, safe=False)

def MenusView(request):
        queryset = Ritz.objects.all().values('plat', 'temps_de_preparation', 'cout')
        return JsonResponse(list(queryset),safe=False)

def DJView(request):
        queryset = Ritz.objects.all().values('plat', 'temps_de_preparation', 'cout')
        return JsonResponse(list(queryset),safe=False)
