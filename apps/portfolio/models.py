from django.db import models


from django.contrib.auth import get_user_model

User = get_user_model()


class Asset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assets")
    ticker = models.CharField(max_length=20)
    quantity = models.IntegerField()
    average_price = models.FloatField()
    current_price = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.ticker:
            self.ticker = self.ticker.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticker} ({self.user.username})"
