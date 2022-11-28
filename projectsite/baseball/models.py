from django.db import models
from django.utils import timezone


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
    team_pic = models.ImageField(default="defaultimg.png", null=True, blank=True, verbose_name="Team Image")
    

class Play(Basemodel):
    STRING_CHOICES= (
    ('First String', 'First String'),
    ('Second String','Second String'))
    player = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = "Player")
    team = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = "Team")
    string_no = models.CharField(max_length=100, choices = STRING_CHOICES)
    isActive = models.BooleanField(default=False)
    pos = models.ForeignKey(Position, on_delete=models.CASCADE)

class Match(Basemodel):
    team1 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = "Team1")
    team2 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = "Team2")
    score_t1 = models.IntegerField()
    score_t2 = models.IntegerField()
    winner = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = "Winner")
    game_date = models.DateField(default=timezone.now, blank=True, verbose_name="Date of Issuance")

# Create your models here.
