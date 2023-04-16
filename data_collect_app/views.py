from django.shortcuts import render
from .models import CollectModel
from .forms import CollectForms
# Create your views here.
def collect(request):
    if request.method == "POST":
        form = CollectForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            team = form.cleaned_data['team']
            age = form.cleaned_data['age']
            object = CollectModel(name = name,team = team, age = age)
            object.save()
    else:
        form = CollectForms()
    return render(request, 'collect.html', {'form': form})