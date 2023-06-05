from django.shortcuts import render

# views.py

# Add this cats list below the imports
finches = [
  {'name': 'Loki', 'species': 'Red Crossbill', 'description': 'happy and loud', 'age': 3},
  {'name': 'Puchi', 'species': 'Evening Grosbeak', 'description': 'cute and colorful', 'age': 2},
]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })
