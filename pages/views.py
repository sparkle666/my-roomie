from django.views.generic import TemplateView
from accounts.models import CustomUser
from django.shortcuts import redirect, render, get_object_or_404
from .forms import FirstOnboardingForm, FourthOnboardingForm, SecondOnboardingForm, ThirdOnboardingForm


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


def mate_results(request):
    return render(request, "pages/onboarding/mate_results.html", {})
