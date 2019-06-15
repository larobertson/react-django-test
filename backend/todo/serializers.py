# We use serializers to convert model instances to JSON for the frontend

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    # The model we want to work with
    model = Todo
    # the fields to convert to JSON
    fields = ('id', 'title', 'description', 'completed')