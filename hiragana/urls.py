from django.urls import path
from .views import HiraganaListView, HiraganaPracticeView


urlpatterns = []
urlpatterns = [
  path(r'hiragana', HiraganaListView.as_view()),
  path(r'hiragana/practice', HiraganaPracticeView.as_view()),
]