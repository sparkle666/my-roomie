from django.urls import reverse
from django.views.generic import TemplateView
from accounts.models import CustomUser
from django.shortcuts import redirect, render, get_object_or_404
from .forms import FirstOnboardingForm, FourthOnboardingForm, SecondOnboardingForm, SuperuserCreationForm, ThirdOnboardingForm
from django.contrib import auth
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


def onboarding_1(request):
    user = get_object_or_404(CustomUser, id=request.user.id)

    if request.method == 'POST':

        form = FirstOnboardingForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('onboarding_2')  # Redirect to a success page
    else:
        form = FirstOnboardingForm()

    return render(request, "pages/onboarding/1.html", {'form': form})


def onboarding_2(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    if request.method == 'POST':
        form = SecondOnboardingForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('onboarding_3')  # Redirect to a success page
    else:
        form = SecondOnboardingForm()

    return render(request, "pages/onboarding/2.html", {'form': form})


def onboarding_3(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    if request.method == 'POST':
        form = ThirdOnboardingForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('onboarding_4')  # Redirect to a success page
    else:
        form = ThirdOnboardingForm()

    return render(request, "pages/onboarding/3.html", {'form': form})


def onboarding_4(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    if request.method == 'POST':
        form = FourthOnboardingForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('mate_results')  # Redirect to a success page
    else:
        form = FourthOnboardingForm()

    return render(request, "pages/onboarding/4.html", {'form': form})


def mate_list(request):
    return render(request, "pages/mate_list.html", {})


# def mate_results(request):
#     current_user = request.user

#     # Get the current user's smoking and cleanliness preferences
#     current_smoking_preference = current_user.smoking_preference
#     current_cleanliness_preference = current_user.cleanliness_level
#     current_location = current_user.location

#     # Exclude the current user from potential matches
#     potential_roommates = CustomUser.objects.exclude(pk=current_user.pk)

#     # Filter potential matches based on smoking and cleanliness preferences
#     matches = potential_roommates.filter(location__icontains=current_location, smoking_preference=current_smoking_preference,
#                                          cleanliness_level=current_cleanliness_preference)

#     return render(request, "pages/onboarding/mate_results.html", {"matches": matches})

def mate_results(request):
    current_user = request.user

    # Get the current user's smoking and cleanliness preferences
    current_smoking_preference = current_user.smoking_preference
    current_cleanliness_preference = current_user.cleanliness_level
    current_location = current_user.location

    # Exclude the current user from potential matches
    potential_roommates = CustomUser.objects.exclude(pk=current_user.pk)

    # Build the OR condition for matching any one of the criteria
    or_condition = Q(location__icontains=current_location) | Q(smoking_preference=current_smoking_preference) | Q(cleanliness_level=current_cleanliness_preference)

    # Filter potential matches based on the OR condition
    matches = potential_roommates.filter(or_condition)

    return render(request, "pages/onboarding/mate_results.html", {"matches": matches})

def superuser_signup(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.is_staff = True
            user.save()

            # Log in the superuser
            user = auth.authenticate(
                username=user.username, password=request.POST['password1'])
            if user is not None:
                auth.login(request, user)

            # Redirect to the admin dashboard.
            return redirect(reverse('admin:index'))
    else:
        form = SuperuserCreationForm()
    return render(request, 'account/superuser_signup.html', {'form': form})
