from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Count
from .models import FoodItem, Vote

# --- Authentication Views ---

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu:food_list')
    else:
        form = UserCreationForm()
    return render(request, 'menu/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu:food_list')
    else:
        form = AuthenticationForm()
    return render(request, 'menu/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('menu:food_list')

# --- Core Application Views ---

def food_list_view(request):
    food_items = FoodItem.objects.annotate(vote_count=Count('vote')).order_by('-vote_count')

    user_votes = []
    if request.user.is_authenticated:
        user_votes = Vote.objects.filter(user=request.user).values_list('food_item_id', flat=True)

    context = {
        'food_items': food_items,
        'user_votes': list(user_votes),
    }
    return render(request, 'menu/menu.html', context)

@login_required
def vote_view(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    if request.method == 'POST':
        try:
            Vote.objects.create(user=request.user, food_item=food_item)
        except IntegrityError:
            pass # User has already voted.
    return redirect('menu:food_list')