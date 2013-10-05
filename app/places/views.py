from django.shortcuts import render
from rest_framework.generics import *
from app.places.models import *

# Create your views here.

class Search(ListAPIView):
	model = Place

	def get_queryset(self):
		places = Place.objects.all()
		if 'q' in self.request.QUERY_PARAMS:
			places.filter(name__icontains=self.request.QUERY_PARAMS['q'])
		return places

