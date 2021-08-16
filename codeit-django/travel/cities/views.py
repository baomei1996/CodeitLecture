from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'cities/index.html')

def city_detail(request, city):
  if city == 'seoul':
    return render(request, 'cities/seoul.html')
  elif city == 'paris':
    return render(request, 'cities/paris.html')
  elif city == 'tokyo':
    return render(request, 'cities/tokyo.html')
  