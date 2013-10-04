from django.contrib.gis.db import models
import us as usa
from django.contrib.auth import get_user_model

#` Create your models here.

class Place(models.Model):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255, unique=True)
	location = models.PointField(geography=True)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2, choices=tuple((x.abbr, x.name) for x in usa.states.STATES_AND_TERRITORIES))
	zip_code = models.CharField(max_length=5)
	points = models.IntegerField(default=0)

class Report(models.Model):
	place = models.ForeignKey(Place, related_name='reports')
	user = models.ForeignKey
	vote = models.IntegerField()
	comment = models.TextField()
