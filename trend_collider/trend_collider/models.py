from django.db import models


class Account(models.Model):
    # Add reference to auth user here
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    username = models.CharField(max_length=25)

    def __str__(self):
        return self.username


class Weigh_In(models.Model):
    account_id = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='weigh_ins')
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    date = models.DateField()
    weight = models.FloatField()

    def __str__(self):
        return self.date


class Stock_Pick(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    symbol = models.CharField(max_length=5)

    def __str__(self):
        return self.symbol
