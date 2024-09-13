from django.db import models

class Utilisateur(models.Model):
    pseudo = models.CharField(max_length=50)

    class Meta:
        ordering = ["pseudo"]

    def __str__(self):
        return self.pseudo

class Ritz(models.Model):
    plat  = models.CharField(max_length=50)
    temps_de_preparation = models.CharField(max_length=50)
    cout = models.CharField(max_length=50)

    def __str__(self):
        return self.plat
    
class After(models.Model):
    jour = models.DateTimeField()
    ritz = models.ManyToManyField(Ritz)
    participants = models.ManyToManyField(Utilisateur, through='Utilisateur_After')

    def __str__(self):
        return str(self.jour)

class Utilisateur_After(models.Model):
    fk_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    fk_After = models.ForeignKey(After, on_delete=models.CASCADE)
    est_DJ = models.BooleanField()
    def __str__(self):
        return f"{self.fk_utilisateur} at {self.fk_After} (DJ: {self.est_DJ})"
