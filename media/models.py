from django.contrib.gis.db import models
from Cities.models import Country,City
# Create your models here.
class Location(models.Model):
    location = models.PointField()
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    city =  forms.ModelChoiceField(queryset=City.objects.none())
    
    #filter the city to country choice
    def __init__(self,*args, **kwargs):
        country = kwargs.pop('country_instance',None)
        super().__init__(*args, **kwargs)
        if country_instance:
            self.fields
    def__str__(self):
        return str(self.location)
    
    
    
