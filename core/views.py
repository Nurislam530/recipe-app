from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe as Recipes
from .models import Comment
from .forms import RecipeForm, CommentForm

def index(request):
    recipes = Recipes.objects.all()
    context = {
        "recipes": recipes
    }  
    return render(request, 'core/index.html', context)

def detail(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    comment = Comment.objects.filter(recipe_id=pk)
    sum_of_stars = 0
    if len(comment) != 0:
        for com in comment:
            sum_of_stars += com.stars
        sum_of_stars = sum_of_stars/len(comment)
        rounded_sum = round(sum_of_stars, 1)
    submitted = False
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.recipe = recipe
            obj.save()
            return HttpResponseRedirect('?submitted=True')
    elif 'submitted' in request.GET:
        submitted = True
    form = CommentForm() 
    return render(request, 'core/detail.html', { "recipe": recipe, "comment": comment,'form': form, 'submitted': submitted, 'sum_of_stars': rounded_sum})

def addRecipe(request):
    submitted = False
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return HttpResponseRedirect('?submitted=True')
    elif 'submitted' in request.GET:
        submitted = True
    form = RecipeForm()
    return render(request, 'core/addRecipe.html', {'form': form, 'submitted': submitted})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Login or password are incorrect, Try Again"))
            return redirect('login')
    else:
        return render(request, 'core/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('index')

def my_recipes(request, author_id):
    if author_id is not None:
        recipes = Recipes.objects.filter(author_id=author_id)
        return render(request, 'core/my_recipes.html', {'recipes':recipes})
    else:
        messages.success(request, ("You need to login first of all!"))
        return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration succesfull!"))
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'core/register_user.html', {'form': form})

