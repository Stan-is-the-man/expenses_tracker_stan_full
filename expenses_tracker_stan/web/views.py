from django.shortcuts import render, redirect

from expenses_tracker_stan.web.forms import CreateProfileForm, EditProfileForm
from expenses_tracker_stan.web.models import Profile, Expense


# extra def:
def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def index_page(request):
    profile = get_profile()
    if not profile:
        return redirect('profile create')  # redirect is to url

    return render(request, 'home-with-profile.html')


def expense_create(request):
    return render(request, 'expense-create.html')


def expense_edit(request, pk):
    return render(request, 'expense-edit.html')


def expense_delete(request, pk):
    return render(request, 'expense-delete.html')


def profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    total_items_bought = len(expenses)
    budget_left = profile.budget - sum(expense.price for expense in expenses)

    context = {
        'profile': profile,
        'total_items_bought': total_items_bought,
        'budget_left': budget_left,
    }

    return render(request, 'profile.html', context)


# extra def:
def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index page')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'POST':
        # podavame i koi tochno profil za edit
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    return render(request, 'profile-delete.html')
