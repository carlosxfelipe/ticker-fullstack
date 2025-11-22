from apps.portfolio.models import Asset
from django.contrib.auth import get_user_model

User = get_user_model()


user, _ = User.objects.get_or_create(
    username="carlos@email.com",
    email="carlos@email.com",
    defaults={"password": "123456"},
)

assets = [
    Asset(
        user=user, ticker="PETR4", quantity=10, average_price=28.5, current_price=30.1
    ),
    Asset(
        user=user, ticker="VALE3", quantity=5, average_price=65.0, current_price=67.2
    ),
    Asset(
        user=user, ticker="ITUB4", quantity=20, average_price=25.0, current_price=26.3
    ),
    Asset(
        user=user, ticker="BBDC4", quantity=15, average_price=23.5, current_price=24.0
    ),
    Asset(
        user=user, ticker="ABEV3", quantity=30, average_price=14.2, current_price=15.0
    ),
]

Asset.objects.filter(user=user).delete()
Asset.objects.bulk_create(assets, ignore_conflicts=True)
print("Seeding completed successfully!")
