from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


BREAD_CHOICE = (
    ('white', 'white'),
    ('hati', 'hati'),
    ('parmesanOregano', 'parmesanOregano'),
    ('honeyOats', 'honeyOats'),
)
MENU_CHOICE = (
    ('shrimp', 'shrimp'),
    ('chicken', 'chicken'),
    ('pork', 'pork'),
    ('beef', 'beef'),
    ('tuna', 'tuna'),
)

CHEESE_CHOICE = (
    ('mozzarella', 'mozzarella'),
    ('cheddar', 'cheddar'),
    ('americanCheese', 'americanCheese'),
)
VEGE_CHOICE = (
    ('Lettuce', 'Lettuce'),
    ('Tomatoes', 'Tomatoes'),
    ('Cucumbers', 'Cucumbers'),
    ('Peppers', 'Peppers'),
    ('RedOnions', 'RedOnions'),
    ('Pickles', 'Pickles'),
    ('Olives', 'Olives'),
    ('Jalapenos', 'Jalapenos')
)

SAUCE_CHOICE = (
    ('Ranch', 'Ranch'),
    ('SweetChilli', 'SweetChilli'),
    ('HoneyMustard', 'HoneyMustard'),
    ('SweetOnion', 'SweetOnion'),
    ('Mayonnaise', 'Mayonnaise'),
    ('SmokeBBQ', 'SmokeBBQ'),
    ('Horseradish', 'Horseradish'),
)
# Create your models here.
class Sandwich(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.CharField(choices=MENU_CHOICE, max_length=100)
    bread = models.CharField(choices=BREAD_CHOICE, max_length=100)
    cheese = models.CharField(choices=CHEESE_CHOICE, max_length=100)
    tosting = models.BooleanField()
    vegetables = MultiSelectField(choices=VEGE_CHOICE, max_length=100, null=True, blank=True)
    sauce = MultiSelectField(choices=SAUCE_CHOICE, max_length=100, null=True, max_choices=3, blank=True)