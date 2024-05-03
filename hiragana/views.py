import random
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Hiragana
from .serializers import HiraganaSerializer


class HiraganaListView(generics.ListAPIView):
  queryset = Hiragana.objects.all()
  permission_classes = [AllowAny]
  serializer_class = HiraganaSerializer

  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)


class HiraganaPracticeView(generics.RetrieveAPIView):
  queryset = Hiragana.objects.order_by('?').all()
  permission_classes = [AllowAny]
  serializer_class = HiraganaSerializer

  def get_object(self):
    return self.get_queryset().first()

  def get(self, request, *args, **kwargs):
    hiragana = self.get_object()
    answers = [
      {
        'pronunciation': hiragana.pronunciation,
        'answer': True
      }
    ]

    for row in self.get_queryset().exclude(pk=28)[:4]:
      answers.append({
        'pronunciation': row.pronunciation,
        'answer': False
      })

    random.shuffle(answers)

    resp = {
      'id': hiragana.id,
      'word': hiragana.word,
      'answers': answers
    }

    return Response(resp)