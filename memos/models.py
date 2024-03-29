from django.db import models
from conf.models import BaseModel, SoftDeleteModel


class Memo(BaseModel, SoftDeleteModel):
  user = models.ForeignKey(
    'users.User',
    on_delete=models.DO_NOTHING,
    db_constraint=False,
    default=None,
    null=True,
    related_name='memos'
  )
  body = models.TextField('본문')
  class Meta:
    db_table = 'memos'
    ordering = ['-id']
    indexes = []
  
  def __str__(self):
    return f'{self.id}'