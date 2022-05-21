from .models import User, Skills
from .forms import SignUpForm, SignInForm, UpdateBasicSkills, UpdateUserBasicSkills

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import RequestContext


def all_users(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, 'home.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'sign_up.html', context)


def sign_in_view(request):
    error = None

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            error = 'Email or password is incorrect'
    else:
        form = SignInForm()
    context = {
        'form': form,
        'error': error
        }
    return render(request, 'sign_in.html', context)


@login_required
def sign_out_view(request):
    logout(request)
    return redirect('home')


@login_required()
def profile_view(request):
    return render(request, 'profile.html')


@login_required()
def basic_skill_view(request):
    basic_skill_ids = [basic_skill.id for basic_skill in User.objects.get(id=request.user.id).basic_skills.all()]
    if request.method == 'POST':
        user_basic_skills = UpdateUserBasicSkills(request.POST)
        new_basic_skills = UpdateBasicSkills(request.POST)
        if user_basic_skills.is_valid() and new_basic_skills.is_valid():
            user_basic_skills.basic_skills(
            request.user, user_basic_skills.cleaned_data.get('basic_skills'),
            new_basic_skills.get_basic_skills())
            return redirect('profile')
    else:
        user_basic_skills = UpdateUserBasicSkills(
        initial={"basic_skills": basic_skill_ids})
        new_basic_skills = UpdateBasicSkills()
    context = {
        'user_basic_skills': user_basic_skills,
        'new_basic_skills': new_basic_skills,
    }
    return render(request, 'basic_skill.html', context=context)
