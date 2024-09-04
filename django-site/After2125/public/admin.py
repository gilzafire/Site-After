from django.contrib import admin
from .models import Utilisateur, After, Ritz, Utilisateur_After

admin.site.register(Utilisateur)
admin.site.register(Ritz)

class DJPseudoFilter(admin.SimpleListFilter):
    title = 'DJ Pseudo'
    parameter_name = 'dj_pseudo'

    def lookups(self, request, model_admin):
        utilisateurs = Utilisateur.objects.filter(
            utilisateur_after__est_DJ=True
        ).distinct()
        return [(utilisateur.pseudo, utilisateur.pseudo) for utilisateur in utilisateurs]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                utilisateur_after__fk_utilisateur__pseudo=self.value(),
                utilisateur_after__est_DJ=True
            )
        return queryset
    
class UtilisateurInLine(admin.TabularInline):
    model = Utilisateur_After
    extra = 1  

@admin.register(After)
class AfterAdmin(admin.ModelAdmin):
    list_display = ('jour',)
    list_filter = ('jour', 'ritz', DJPseudoFilter)
    inlines = [
        UtilisateurInLine
    ]


    
# Register your models here.
