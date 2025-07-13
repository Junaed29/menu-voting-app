from django.contrib import admin
from .models import FoodItem, Ingredient, Vote


class IngredientInline(admin.TabularInline):
    model = FoodItem.ingredients.through
    extra = 1


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    inlines = [IngredientInline]
    exclude = ("ingredients",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "food_item")
    search_fields = ("user__username", "food_item__name")
