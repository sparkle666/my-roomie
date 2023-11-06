from django.urls import path

from .views import (HomePageView, mate_results, onboarding_1,
                    onboarding_2, onboarding_3, onboarding_4)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("onboarding/1/", onboarding_1, name="onboarding_1"),
    path("onboarding/2/", onboarding_2, name="onboarding_2"),
    path("onboarding/3/", onboarding_3, name="onboarding_3"),
    path("onboarding/4/", onboarding_4, name="onboarding_4"),
    path("results/", mate_results, name="mate_results"),

]
