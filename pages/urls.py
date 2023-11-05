from django.urls import path

from .views import (HomePageView, onboarding_1, onboarding_2)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("onboarding/1/", onboarding_1, name="onboarding_1"),
    path("onboarding/2/", onboarding_2, name="onboarding_2"),

]
