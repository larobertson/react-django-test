# We use serializers to convert model instances to JSON for the frontend

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo # The model we want to work with
    fields = ('id', 'title', 'description', 'completed') # the fields to convert to JSON