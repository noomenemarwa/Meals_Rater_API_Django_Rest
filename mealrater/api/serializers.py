from rest_framework import serializers
from.models import Meal, Rating

# Meal serializer
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model=Meal
        fields =('id','title','description')

# Rating serializer
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'meal')
       