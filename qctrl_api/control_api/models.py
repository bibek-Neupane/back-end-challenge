from django.db import models

class Control(models.Model):

    objects=models.Manager()

    TYPE_CHOICES=(
        ('Primitive','Primitive'),
        ('Corpse','CORPSE'),
        ('Gaussian','Gaussian'),
        ('CinBB','CinBB'),
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES, default='Primitive' )
    maximum_rabi_rate = models.FloatField()
    polar_angle = models.FloatField()

