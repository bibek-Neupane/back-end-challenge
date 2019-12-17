from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Control(models.Model):

    objects=models.Manager()

    TYPE_CHOICES=(
        ('Primitive','Primitive'),
        ('Corpse','CORPSE'),
        ('Gaussian','Gaussian'),
        ('CinBB','CinBB'),
    )
    #pk i.e id --> Refered to as pk while we use it as a lookup variable
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES, default='Primitive')
    maximum_rabi_rate = models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(100)])
    polar_angle = models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self):
        return self.name

