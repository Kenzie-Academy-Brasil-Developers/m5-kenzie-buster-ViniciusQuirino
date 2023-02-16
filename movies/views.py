from django.shortcuts import render
from rest_framework.views import APIView, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from movies.serializers import MovieSerializer, OrderMovieSerializer
from django.shortcuts import get_object_or_404
from .models import Movie
from .permissions import IsEmployee
import ipdb

# Autenticação -> diz sobre quem está acessando a rota
# Permissão / Autorização -> restringe o acesso a determinado recurso


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployee]

    def get(self, request: Request) -> Response:
        users = Movie.objects.all()

        serializer = MovieSerializer(users, many=True)

        return Response(serializer.data, 200)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(added_by=request.user)
        return Response(serializer.data, 201)


class OrderMovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = OrderMovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie=movie, user=request.user)

        return Response(serializer.data,201)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response(status=204)
