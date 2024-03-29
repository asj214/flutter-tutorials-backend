from rest_framework.routers import DefaultRouter
from .views import MemoViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'memos', MemoViewSet)

urlpatterns = []
urlpatterns += router.urls