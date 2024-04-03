from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from conf.permissions import ReadOnlyIfNotAuthenticatedOrOwner
from .models import Memo
from .serializers import MemoSerializer


class MemoViewSet(viewsets.ModelViewSet):
  permission_classes = [ReadOnlyIfNotAuthenticatedOrOwner]
  serializer_class = MemoSerializer
  queryset = Memo.objects.prefetch_related('user').all()

  def get_queryset(self):
    return self.queryset
    
  def get_object(self, pk=None):
    try:
      return self.queryset.get(pk=pk)
    except Memo.DoesNotExist:
      raise NotFound('Not Found')
  
  def list(self, request, *args, **kwargs):
    page = self.paginate_queryset(self.get_queryset())
    serializer = self.get_serializer(page, many=True)
    return self.get_paginated_response(serializer.data)
    
  def create(self, request, *args, **kwargs):
    context = {
      'user': request.user,
    }
    serializer = self.serializer_class(
      data=request.data,
      context=context,
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  def retrieve(self, request, pk=None, *args, **kwargs):
    memo = self.get_object(pk)
    serializer = self.serializer_class(memo)

    return Response(serializer.data)
    
  def update(self, request, pk=None, *args, **kwargs):
    memo = self.get_object(pk)
    self.check_object_permissions(self.request, memo)
    serializer = self.serializer_class(
      memo,
      data=request.data,
      context={'user': request.user},
      partial=True
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)
    
  def destroy(self, request, pk=None, *args, **kwargs):
    memo = self.get_object(pk)
    self.check_object_permissions(self.request, memo)
    memo.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)