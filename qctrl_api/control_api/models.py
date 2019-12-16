from django.db import models

class Control(models.Model):

    TYPE_CHOICES=(
        ('Primitive','Primitive'),
        ('Corpse','Corpse'),
        ('Gaussian','Gaussian'),
        ('CinBB','CinBB'),
    )

    name = models.CharField(max_length=200)
    control_type = models.CharField(max_length=200, choices=TYPE_CHOICES, )
    maximum_rabi_rate = models.FloatField()
    polar_angle = models.FloatField()

