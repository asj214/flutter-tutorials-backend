from rest_framework import serializers
from .models import Hiragana


class HiraganaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hiragana
    fields = (
      'id',
      'word',
      'pronunciation',
    )
