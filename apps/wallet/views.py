from django.shortcuts import render, redirect, get_object_or_404


def wallet_home(request):
    from apps.portfolio.models import Asset

    assets = Asset.objects.filter(user=request.user)
    return render(request, "wallet/wallet.html", {"assets": assets})


def wallet_create(request):
    from apps.portfolio.models import Asset

    if request.method == "POST":
        ticker = request.POST.get("ticker")
        quantity = request.POST.get("quantity")
        average_price = request.POST.get("average_price")
        Asset.objects.create(
            user=request.user,
            ticker=ticker,
            quantity=quantity,
            average_price=average_price,
        )
        return redirect("wallet:home")
    return render(request, "wallet/create.html")


def wallet_edit(request, id):
    from apps.portfolio.models import Asset

    asset = get_object_or_404(Asset, id=id, user=request.user)
    if request.method == "POST":
        asset.ticker = request.POST.get("ticker")
        asset.quantity = request.POST.get("quantity")
        asset.average_price = request.POST.get("average_price")
        asset.save()
        return redirect("wallet:home")
    return render(request, "wallet/edit.html", {"asset": asset})


def wallet_delete(request, id):
    # Apenas redireciona para a home por enquanto
    return redirect("wallet:home")
