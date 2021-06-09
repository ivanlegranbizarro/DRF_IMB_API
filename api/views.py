from django.shortcuts import render
from rest_framework import generics
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class ListMovieView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 1
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['title', 'genre__name', 'language', 'type_movie']


class CreateMovieView(generics.CreateAPIView):
    serializer_class = MovieSerializer


class RetrieveMovieView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    lookup_field = 'title'
    serializer_class = MovieSerializer


class ListCreateGenreView(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    pagination_class = PageNumberPagination
    pagination_class.page_size = 1
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['name', ]
