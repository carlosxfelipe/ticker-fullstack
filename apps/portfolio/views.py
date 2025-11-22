from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    assets = list(user.assets.all())
    assets.sort(key=lambda a: a.quantity * a.current_price, reverse=True)
    labels = [asset.ticker for asset in assets]
    values = [asset.quantity * asset.current_price for asset in assets]
    return render(
        request,
        "portfolio/portfolio.html",
        {
            "labels": labels,
            "values": values,
        },
    )
