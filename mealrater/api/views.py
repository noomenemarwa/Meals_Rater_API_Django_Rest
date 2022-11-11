from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal, Rating
from .serializers import MealSerializer,RatingSerializer

# viewsets for Meal
class MealViewSet(viewsets.ModelViewSet):
    # get all Meal objects
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
   

# viewsets for Rating
class RatingViewSet(viewsets.ModelViewSet):
    # get all Rating objects
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer