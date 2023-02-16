from rest_framework import serializers
from .models import MovieOrder, Seasons
from .models import Movie
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True)
    rating = serializers.ChoiceField(choices=Seasons.choices, default=Seasons.G)
    synopsis = serializers.CharField(allow_null=True)

    added_by = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Movie:
        # ipdb.set_trace()
        return Movie.objects.create(**validated_data)

    def get_added_by(self, obj):
        added_by = obj.added_by.email
        return added_by


class OrderMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.FloatField()
    buyed_at = serializers.DateTimeField(read_only=True)

    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()

    def get_buyed_by(self, obj):
        buyed_by = obj.user.email
        return buyed_by

    def get_title(self, obj):
        title = obj.movie.title
        return title

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
