# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Ingredient(models.Model):
    _name = 'myhealthydiet.ingredient'
    
#   VARIABLES
    name = fields.Char(required=True, help="Name of the ingredient", string="Ingredient")
    foodTypeEnum = fields.Selection([("VEGETABLE", "VEGETABLE"), ("FRUIT", "FRUIT"),
    ("NUT", "NUT"), ("GRAIN", "GRAIN"), ("BEAN", "BEAN"), ("MEAT", "MEAT"),
    ("POULTRY", "POULTRY"), ("FISH", "FISH"), ("SEAFOOD", "SEAFOOD"), ("DAIRY", "DAIRY")], required=True, 
    help="Type of food: VEGETABLE, FRUIT, NUT, GRAIN, BEAN, MEAT, POULTRY, FISH, SEAFOOD, DAIRY")
    isInSeason = fields.Boolean(required=True, help="Boolean that shows if it is in season or not")
    waterIndex = fields.Float(required=True, help="Float that shows the porcentage of water of the ingredient")
    
#   RELATIONS
    plates = fields.Many2many('myhealthydiet.plate', string="Plates", required=True, help="Plates")

    @api.onchange('waterIndex')
    def _onchange_waterIndex(self):
        if self.waterIndex > 100.0 or self.waterIndex < 0.0:
            return {
                'warning': {
                    'title': "Something bad happend",
                    'message': "That value is not accepted",
            }
        }
    
    @api.constrains('waterIndex')
    def _check_something(self):
        if self.waterIndex > 100.0 or self.waterIndex < 0.0:
            raise ValidationError("That values are not accepted")