from django.shortcuts import render

# Create your views here.


def home(request):
    user = request.user
    assets = []
    if user.is_authenticated:
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
