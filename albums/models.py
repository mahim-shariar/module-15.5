from django.db import models
from musician_directory.models import muisician

# Create your models here.

class Album(models.Model):
    Album_name = models.CharField(max_length=50)
    Artist_name =models.ForeignKey(muisician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    
    def __str__(self):
        return self.Album_name
    