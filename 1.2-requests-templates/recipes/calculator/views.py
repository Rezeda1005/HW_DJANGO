from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def show_recipe(request, dish):
    recipe = DATA.get(dish)
    servings = request.GET.get('servings') or 1
    final_recipe = {}
    for key, value in recipe.items():
        final_recipe[key] = round((value * int(servings)), 3)
    context = {
       'recipe_name': dish,
       'recipe': final_recipe,
    }

    return render(request, 'calculator/index.html', context)