from django.contrib import admin
from django.contrib.admin import display
from .models import Position, Person, Club, Play

# Register your models here.


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "height", "weight")
    search_fields = ("last_name", "first_name", "height", "weight")


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name", "coach", "dorm_latitude", "dorm_longtitude")
    search_fields = ("name", "coach", "dorm_latitude", "dorm_longtitude")

@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ("player","team","string_no","isActive",)
