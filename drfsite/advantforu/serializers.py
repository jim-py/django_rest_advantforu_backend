from rest_framework import serializers
from .models import Post, Portfolio, PhotosPortfolio, Service


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class PhotosPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotosPortfolio
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
