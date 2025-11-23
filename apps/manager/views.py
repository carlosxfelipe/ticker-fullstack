from django.shortcuts import render, redirect, get_object_or_404


def manager_home(request):
    from apps.portfolio.models import Asset

    assets_queryset = Asset.objects.filter(user=request.user)
    assets = []
    for asset in assets_queryset:
        try:
            if asset.average_price and asset.average_price != 0:
                percent_change = (
                    (asset.current_price - asset.average_price) / asset.average_price
                ) * 100
            else:
                percent_change = None
        except Exception:
            percent_change = None
        total_invested = None
        try:
            if asset.quantity is not None and asset.average_price is not None:
                total_invested = float(asset.quantity) * float(asset.average_price)
        except Exception:
            total_invested = None
        current_value = None
        try:
            if asset.quantity is not None and asset.current_price is not None:
                current_value = float(asset.quantity) * float(asset.current_price)
        except Exception:
            current_value = None
        result = None
        if current_value is not None and total_invested is not None:
            result = current_value - total_invested
        assets.append(
            {
                "id": asset.id,
                "ticker": asset.ticker,
                "quantity": asset.quantity,
                "average_price": asset.average_price,
                "current_price": asset.current_price,
                "percent_change": percent_change,
                "total_invested": total_invested,
                "current_value": current_value,
                "result": result,
            }
        )
    return render(request, "manager/manager.html", {"assets": assets})


def manager_create(request):
    from apps.portfolio.models import Asset

    if request.method == "POST":
        ticker = request.POST.get("ticker")
        quantity = request.POST.get("quantity")
        average_price = request.POST.get("average_price")
        current_price = request.POST.get("current_price")
        Asset.objects.create(
            user=request.user,
            ticker=ticker,
            quantity=quantity,
            average_price=average_price,
            current_price=current_price,
        )
        return redirect("manager:home")
    return render(request, "manager/create.html")


def manager_edit(request, id):
    from apps.portfolio.models import Asset

    asset = get_object_or_404(Asset, id=id, user=request.user)
    if request.method == "POST":
        asset.ticker = request.POST.get("ticker")
        asset.quantity = request.POST.get("quantity")
        asset.average_price = request.POST.get("average_price")
        asset.current_price = request.POST.get("current_price")
        asset.save()
        return redirect("manager:home")
    return render(request, "manager/edit.html", {"asset": asset})


def manager_delete(request, id):
    from apps.portfolio.models import Asset

    asset = get_object_or_404(Asset, id=id, user=request.user)
    if request.method == "POST":
        asset.delete()
    return redirect("manager:home")
