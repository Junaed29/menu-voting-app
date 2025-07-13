from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):  # Provides a human-readable name in the admin panel
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="food_images/")
    ingredients = models.ManyToManyField(Ingredient)  # Creates the many-to-many link

    def __str__(self):
        return self.name


class Vote(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Creates a one-to-manylink to User
    food_item = models.ForeignKey(
        FoodItem, on_delete=models.CASCADE
    )  # Creates a one-to-many link to FoodItem

    class Meta:
        # This database constraint is the key to our "vote only once" rule.
        # It tells the database that the combination of a user and a food item must be unique.
        unique_together = ("user", "food_item")

    def __str__(self):
        return f"{self.user.username} voted for {self.food_item.name}"
