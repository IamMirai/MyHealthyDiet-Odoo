# -*- coding: utf-8 -*-

from odoo import models, fields

class ingredient(models.Model):
    _name = 'myhealthydiet.ingredient'
    
    ingredient_id = fields.Integer(required=True, help="Id of the ingredient")
    ingredientName = fields.Char(required=True, help="Name of the ingredient")
    foodTypeEnum = fields.Selection([("VEGETABLE", "VEGETABLE"), ("FRUIT", "FRUIT"), ("NUT", "NUT"), ("GRAIN", "GRAIN"), ("BEAN", "BEAN"), ("MEAT", "MEAT"),
    ("POULTRY", "POULTRY"), ("FISH", "FISH"), ("SEAFOOD", "SEAFOOD"), ("DAIRY", "DAIRY")], required=True, 
    help="Type of food: VEGETABLE, FRUIT, NUT, GRAIN, BEAN, MEAT, POULTRY, FISH, SEAFOOD, DAIRY")
    plates = fields.Many2many('myhealthydiet.plate')
    isInSeason = fields.boolean(required=True, help="Boolean that shows if it is in season or not")
