from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import InquiryForm


SERVICE_PAGES = {
    "legacy": {
        "number": "01",
        "title": "Legacy",
        "tag": "Signature",
        "image": "images/portfolio/legacy-erin.jpg",
        "alt": "Legacy portrait with refined studio lighting",
        "intro": "Fine art portraits designed for personal history, family memory, and heirloom wall artwork.",
        "body": [
            "Legacy sessions are built for families and individuals who want portraits that feel permanent, considered, and worthy of being displayed.",
            "The experience moves slowly enough to understand the people, relationships, and details that should shape the finished artwork.",
        ],
    },
    "celebration": {
        "number": "02",
        "title": "Celebration of Life",
        "tag": "By Invitation",
        "image": "images/portfolio/celebration-hannah-red.jpg",
        "alt": "Hollywood inspired milestone portrait in a red gown",
        "intro": "Thoughtful sessions for honoring a life chapter with dignity, warmth, and intention.",
        "body": [
            "Celebration of Life portraits are shaped around meaning: a milestone, a transition, a relationship, or a season that deserves to be remembered.",
            "Neil guides the pacing, mood, and artwork choices so the result feels personal without ever feeling rushed.",
        ],
    },
    "headshots": {
        "number": "03",
        "title": "Headshots",
        "tag": "Studio",
        "image": "images/portfolio/headshot-greg.jpg",
        "alt": "Cinematic professional headshot portrait",
        "intro": "Professional portraits with refined lighting and presence, made for people who want polish without stiffness.",
        "body": [
            "Headshot sessions focus on presence, expression, and useful finished images for business, creative work, and public profiles.",
            "The direction stays calm and practical, giving you portraits that look polished while still feeling like you.",
        ],
    },
    "dogs": {
        "number": "04",
        "title": "Dogs",
        "tag": "Companion",
        "image": "images/portfolio/dog-dutchess.jpg",
        "alt": "Fine art dog portrait against a painted backdrop",
        "intro": "Artful companion portraits that preserve personality, expression, and the bond clients never want to lose.",
        "body": [
            "Dog portrait sessions are planned around patience, personality, and the connection between people and their companions.",
            "The final artwork is designed to feel affectionate and elevated, with the same fine art care as every portrait experience.",
        ],
    },
}


def home(request):
    return render(request, "homepage.html")


def about(request):
    return render(request, "about.html")


def portraits(request):
    return render(request, "portraits.html")


def services(request):
    return render(request, "services.html")


def service_detail(request, service_slug):
    service = SERVICE_PAGES.get(service_slug)
    if service is None:
        raise Http404("Service not found")
    return render(request, "service_detail.html", {"service": service})


def experience(request):
    return render(request, "experience.html")


def journal(request):
    return render(request, "journal.html")


def model_calls(request):
    return render(request, "model_calls.html")


def booking(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you. Your inquiry has been received.")
            return redirect("booking")
    else:
        form = InquiryForm()

    return render(request, "booking.html", {"form": form})
