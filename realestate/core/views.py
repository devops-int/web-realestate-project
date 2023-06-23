from django.shortcuts import render, redirect

from item.models import Catergory, Item

from .forms import SignupForm

from django.contrib.auth import logout

# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
