from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("portraits/", views.portraits, name="portraits"),
    path("services/", views.services, name="services"),
    path("services/<slug:service_slug>/", views.service_detail, name="service_detail"),
    path("experience/", views.experience, name="experience"),
    path("journal/", views.journal, name="journal"),
    path("model-calls/", views.model_calls, name="model_calls"),
    path("booking/", views.booking, name="booking"),
]
