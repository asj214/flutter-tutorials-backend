from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Memo


class MemoSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)
  body = serializers.CharField()  

  class Meta:
    model = Memo
    fields = (
      'id',
      'user',
      'body',
      'created_at',
      'updated_at'
    )
  
  def create(self, validated_data):
    user = self.context.pop('user')
    return Memo.objects.create(
      user=user,
      **validated_data
    )

  def update(self, instance, validated_data):
    for (key, value) in validated_data.items():
      setattr(instance, key, value)

    instance.save()
    return instance
