from django.shortcuts import render, redirect


def wallet_home(request):
    from apps.portfolio.models import Asset

    # Edição
    ativo_edit = None
    edit_id = request.GET.get("edit")
    if edit_id:
        try:
            ativo_edit = Asset.objects.get(id=edit_id, user=request.user)
        except Asset.DoesNotExist:
            ativo_edit = None

    # Salvar/criar
    if request.method == "POST":
        id_post = request.POST.get("id")
        ticker = request.POST.get("ticker")
        quantity = request.POST.get("quantity")
        average_price = request.POST.get("average_price")
        if id_post:
            # Editar existente
            try:
                ativo = Asset.objects.get(id=id_post, user=request.user)
                ativo.ticker = ticker
                ativo.quantity = quantity
                ativo.average_price = average_price
                ativo.save()
            except Asset.DoesNotExist:
                pass
        else:
            # Criar novo
            Asset.objects.create(
                user=request.user,
                ticker=ticker,
                quantity=quantity,
                average_price=average_price,
            )
        return redirect("wallet:home")

    ativos = Asset.objects.filter(user=request.user)
    return render(
        request, "wallet/wallet.html", {"ativos": ativos, "ativo_edit": ativo_edit}
    )


def wallet_create(request):
    return render(request, "wallet/create.html")


def wallet_edit(request, id):
    return render(request, "wallet/edit.html")


def wallet_delete(request, id):
    # Apenas redireciona para a home por enquanto
    return redirect("wallet:home")


from django.shortcuts import render

# Create your views here.
