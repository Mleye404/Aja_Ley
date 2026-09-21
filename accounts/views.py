from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignUpForm, AddressForm
from .models import Address
from orders.models import Order


class AjaLoginView(LoginView):
    template_name = "accounts/login.html"


class AjaLogoutView(LogoutView):
    next_page = "core:home"


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bienvenue chez AJA LEY, {user.first_name} !")
            return redirect("accounts:profile")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    addresses = Address.objects.filter(user=request.user)
    return render(request, "accounts/profile.html", {"orders": orders, "addresses": addresses})


@login_required
def address_add(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, "Adresse enregistrée.")
            return redirect("accounts:profile")
    else:
        form = AddressForm()
    return render(request, "accounts/address_form.html", {"form": form})
