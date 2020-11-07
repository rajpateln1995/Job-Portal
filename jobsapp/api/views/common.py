from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from ..serializers import *


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobSerializer
    queryset = serializer_class.Meta.model.objects.filter(filled=False)
    permission_classes = [AllowAny]


class SearchApiView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'location' in self.request.GET and 'position' in self.request.GET:
            return self.serializer_class.Meta.model.objects.filter(filled=False, location__contains=self.request.GET['location'],
                                                                   title__contains=self.request.GET['position'])
        else:
            return self.serializer_class.Meta.model.objects.filter(filled=False)
