from django.db import models


class Basemodel (models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Position (Basemodel):
    description = models.CharField(max_length=100)


class Person (Basemodel):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=100, decimal_places=5, null=True)
    weight = models.DecimalField(max_digits=100, decimal_places=5, null=True)


class Club (Basemodel):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(Person, on_delete=models.CASCADE)
    dorm_latitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    dorm_longtitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)

class Play(Basemodel):
    STRING_CHOICES= (
    ('First String', 'First String'),
    ('Second String','Second String'))
    player = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = "Player")
    team = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = "Team")
    string_no = models.CharField(max_length=100, choices = STRING_CHOICES)
    isActive = models.BooleanField(default=False)
    pos = models.ForeignKey(Position, on_delete=models.CASCADE)

# Create your models here.
