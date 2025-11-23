from django.shortcuts import render, redirect, get_object_or_404


def manager_home(request):
    from apps.portfolio.models import Asset

    assets = Asset.objects.filter(user=request.user)
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
        asset.save()
        return redirect("manager:home")
    return render(request, "manager/edit.html", {"asset": asset})


def manager_delete(request, id):
    from apps.portfolio.models import Asset

    asset = get_object_or_404(Asset, id=id, user=request.user)
    if request.method == "POST":
        asset.delete()
    return redirect("manager:home")
