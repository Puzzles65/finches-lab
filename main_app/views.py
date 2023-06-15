from django.shortcuts import render

finches = [
  {'name': 'Tweety', 'species': 'zebra finch', 'description': 'colorful and social', 'age': 1},
  {'name': 'Sunny', 'species': 'goldfinch', 'description': 'vibrant yellow feathers', 'age': 2},
  {'name': 'Bluebell', 'species': 'blue-faced parrot finch', 'description': 'striking blue face and red beak', 'age': 3},
  {'name': 'Pippin', 'species': 'gouldian finch', 'description': 'gorgeous multi-colored plumage', 'age': 2},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })