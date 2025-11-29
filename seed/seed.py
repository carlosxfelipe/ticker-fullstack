from apps.portfolio.models import Asset
from django.contrib.auth import get_user_model

User = get_user_model()


user, created = User.objects.get_or_create(
    username="carlos@email.com",
    email="carlos@email.com",
)
if created:
    user.set_password("123456")
    user.save()

assets = [
    Asset(
        user=user,
        ticker="PETR4",
        quantity=100,
        average_price=31.24,
        current_price=31.79,
    ),
    Asset(
        user=user, ticker="VALE3", quantity=50, average_price=53.45, current_price=67.40
    ),
    Asset(
        user=user,
        ticker="ITUB4",
        quantity=200,
        average_price=37.49,
        current_price=41.64,
    ),
    Asset(
        user=user,
        ticker="BBDC4",
        quantity=150,
        average_price=16.08,
        current_price=19.65,
    ),
    Asset(
        user=user,
        ticker="COCA34",
        quantity=120,
        average_price=67.29,
        current_price=64.77,
    ),
    Asset(
        user=user,
        ticker="AFHI11",
        quantity=80,
        average_price=92.40,
        current_price=94.67,
    ),
    Asset(
        user=user,
        ticker="SNAG11",
        quantity=600,
        average_price=09.67,
        current_price=10.17,
    ),
]

Asset.objects.filter(user=user).delete()
Asset.objects.bulk_create(assets, ignore_conflicts=True)
print("Seeding completed successfully!")
