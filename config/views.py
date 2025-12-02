from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def account_settings(request):
    return render(request, "settings.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)
