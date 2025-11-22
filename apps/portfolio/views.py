from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    assets = user.assets.all()
    labels = [asset.ticker for asset in assets]
    values = [asset.quantity for asset in assets]
    return render(
        request,
        "portfolio/portfolio.html",
        {
            "labels": labels,
            "values": values,
        },
    )
