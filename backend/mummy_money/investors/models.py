from django.db import models
from django.utils.timezone import now

INVESTOR_STATUS = (('ACTIVE', 'Active'), ('NOT_ACTIVE', 'Not Active'))


class Investor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=INVESTOR_STATUS)
    root_privilege = models.BooleanField(default=False)
    funds = models.DecimalField(max_digits=19, decimal_places=2)
    innocence = models.DecimalField(max_digits=3, decimal_places=2)
    experience = models.DecimalField(max_digits=3, decimal_places=2)
    charisma = models.DecimalField(max_digits=3, decimal_places=2)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='investor',
        on_delete=models.SET_NULL
    )
    joining_at = models.DateTimeField(default=now(), editable=False)
    leaving_at = models.DateTimeField(null=True, editable=False)

    class Meta:
        verbose_name = "Investor"
        verbose_name_plural = "Investors"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


