from django.db import models


class Seasons(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(
        max_length=127, choices=Seasons.choices, default=Seasons.G
    )
    synopsis = models.TextField(null=True)

    added_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movie", null=True
    )

    def __str__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}>"


class MovieOrder(models.Model):
    price = models.FloatField()
    buyed_at = models.DateTimeField(auto_now_add=True)  # coprou em

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="order_movie"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_movie"
    )  # comprado por

    def __str__(self) -> str:
        return f"<MovieOrder [{self.id}] - {self.buyed_at}>"
