from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters
from .models import Post, Portfolio, PhotosPortfolio, Service
from .serializers import PortfolioSerializer, PostSerializer, PhotosPortfolio, ServiceSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(mixins.RetrieveModelMixin,  # Просмотр одного объекта
                  mixins.ListModelMixin,  # Просмотр всех объектов
                  GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['id', 'title', 'date']
    ordering = ['-date']
    filterset_fields = ['title', 'short_description', 'description']


class PortfolioViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       GenericViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name']
    ordering = ['-id']
    filterset_fields = ['name', 'description']

    def retrieve(self, *args, **kwargs):
        portfolio = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        serializer = PortfolioSerializer(portfolio)
        res = serializer.data
        photos = []
        for portf in PhotosPortfolio.objects.filter(portfolio=portfolio).order_by('number'):
            photos.append('http://127.0.0.1:8000/media/' + str(portf.photo))
        res['photos'] = photos
        res['photo'] = 'http://127.0.0.1:8000' + res['photo']
        return Response(res)


class ServiceViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'cost']
    ordering = ['-id']
    filterset_fields = ['name', 'description', 'cost']
