# -*- coding: utf-8 -*-

from odoo import models, fields

class Ingredient(models.Model):
    _name = 'myhealthydiet.ingredient'
    
#   VARIABLES
    name = fields.Char(required=True, help="Name of the ingredient", string="Ingredient")
    foodTypeEnum = fields.Selection([("VEGETABLE", "VEGETABLE"), ("FRUIT", "FRUIT"),
    ("NUT", "NUT"), ("GRAIN", "GRAIN"), ("BEAN", "BEAN"), ("MEAT", "MEAT"),
    ("POULTRY", "POULTRY"), ("FISH", "FISH"), ("SEAFOOD", "SEAFOOD"), ("DAIRY", "DAIRY")], required=True, 
    help="Type of food: VEGETABLE, FRUIT, NUT, GRAIN, BEAN, MEAT, POULTRY, FISH, SEAFOOD, DAIRY")
    isInSeason = fields.Boolean(required=True, help="Boolean that shows if it is in season or not")
    
#   RELATIONS
    plates = fields.Many2many('myhealthydiet.plate', string="Plates", required=True, help="Plates")