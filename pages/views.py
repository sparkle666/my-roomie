from django.views.generic import TemplateView
from accounts.models import CustomUser
from django.shortcuts import redirect, render, get_object_or_404
from .forms import FirstOnboardingForm, SecondOnboardingForm

class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


def onboarding_1(request):
    if request.method == 'POST':
        form = FirstOnboardingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('onboarding_2')  # Redirect to a success page
    else:
        form = FirstOnboardingForm()

    return render(request, "pages/onboarding/1.html", {'form': form})

def onboarding_2(request):
    if request.method == 'POST':
        form = SecondOnboardingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = SecondOnboardingForm()

    return render(request, "pages/onboarding/2.html", {'form': form})

