from django.db import models

# Create your models here.
class These(models.Model):
    EtudiantID = models.IntegerField()
    EncadrentID = models.IntegerField()
    Titre = models.CharField(max_length=250)
    Date = models.CharField(max_length=250)
    Duree = models.IntegerField()
    Contenu = models.FileField(upload_to='fichiers/')
    class Meta:
        db_table = "these" 