from __future__ import unicode_literals

from django.db import models
from ..loginreg.models import User
# Create your models here.
class CharacterManager(models.Manager):
    def new_character(self, form_data):
        self.create(name=form_data['name'], alignment=form_data['alignment'],
            race=form_data['race'], char_class=form_data['char_class'],
            level=form_data['level'], exp=form_data['exp'],
            curr_hp=form_data['curr_hp'], max_hp=form_data['max_hp'],
            damage=form_data['damage'], armor=form_data['armor'],
            strength=form_data['strength'], dexterity=form_data['dexterity'],
            constitution=form_data['constitution'], intelligence=form_data['intelligence'],
            wisdom=form_data['wisdom'], charisma=form_data['charisma'])
        return True
    def update_character(self, id, form_data):
        c = self.get(id=id)
        c.name=form_data['name']
        c.alignment=form_data['alignment']
        c.race=form_data['race']
        c.char_class=form_data['char_class']
        c.level=form_data['level']
        c.exp=form_data['exp']
        c.curr_hp=form_data['curr_hp']
        c.max_hp=form_data['max_hp']
        c.damage=form_data['damage']
        c.armor=form_data['armor']
        c.strength=form_data['strength']
        c.dexterity=form_data['dexterity']
        c.constitution=form_data['constitution']
        c.intelligence=form_data['intelligence']
        c.wisdom=form_data['wisdom']
        c.charisma=form_data['charisma']
        c.save()

class Character(models.model):
    ### META ###
    user = models.ForeignKey(User)
    ### INFO ###
    name = models.CharField(max_length=255)
    alignment = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    char_class = models.CharField(max_length=255)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    ### STATS ###
	curr_hp = models.IntegerField()
    max_hp = models.IntegerField()
    damage = models.IntegerField()
    armor = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
