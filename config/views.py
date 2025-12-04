from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_POST


@login_required
def account_settings(request):
    return render(request, "settings.html")


@login_required
@require_POST
def delete_account(request):
    user = request.user
    logout(request)
    user.delete()
    return render(request, "accounts/account_deleted.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)
