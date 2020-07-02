from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status,filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from imdb_prj.pagination import CustomPagination
import coreapi
from rest_framework.schemas import AutoSchema

# Create your views here.

#to add the payload at the swagger interface
class ImdbMovieSchema(AutoSchema):
    def get_manual_fields(self,path,method):
        extra_fields=[]
        if method.lower() in ['post','put']:
            extra_fields=[
                coreapi.Field('name')
            ]
        manual_fields=super().get_manual_fields(path,method)
        #return manual_fields
        return manual_fields + extra_fields


#to add the payload at the swagger interface
class ImdbMovieSchema_2(AutoSchema):
    def get_manual_fields(self,path,method):
        extra_fields=[]
        manual_fields=super().get_manual_fields(path,method)
        return manual_fields



    
class ImdbMovieListAPIView(generics.ListAPIView):
    """
    API view for searching/listing Movies for normal user without credentials
    """
    queryset=queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends=(filters.SearchFilter,)
    search_fields=('name',)



class ImdbMovieViewSet(viewsets.ModelViewSet):
    """all CRUD using router for authorized user only"""
    schema = ImdbMovieSchema_2()

    serializer_class=MovieSerializer
    queryset=Movie.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,IsAdminUser)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name',)





from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MovieList(APIView):
    """List all movies."""

    schema = ImdbMovieSchema()
    

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class MovieCreate(APIView):
    """Create a new movie."""

    schema = ImdbMovieSchema()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,IsAdminUser)

    def post(self, request, format=None):
        
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MovieDetail(APIView):
    """
    Retrieve/detail of a movie, update or delete a movie instance.
    """

    schema = ImdbMovieSchema()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,IsAdminUser)

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie = MovieSerializer(movie)
        return Response(movie.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 



