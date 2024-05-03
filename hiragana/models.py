from django.db import models
from conf.models import BaseModel, SoftDeleteModel


class Hiragana(BaseModel, SoftDeleteModel):
  word = models.CharField('단어', max_length=30, unique=True)
  pronunciation = models.CharField('단어', max_length=30)

  class Meta:
    db_table = 'hiragana'
    ordering = ['id']
    indexes = []
  
  def __str__(self):
    return f'{self.id}'