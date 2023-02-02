# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Ingredient(models.Model):
    _name = 'myhealthydiet.ingredient'
    
#   VARIABLES
    name = fields.Char(string="Ingredient", help="Name of the ingredient", required=True)
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
        
    #@api.onchange('name')
    #def _onchange_name(self):
    #    if len(self.name) > 50:
    #        return {
    #            'warning': {
    #                'title': "Something bad happend",
    #                'message': "The name cannot have more than 50 characters",
    #        }
    #    }
        
    @api.constrains('name')
    def _check_name(self):
        if len(self.name) > 50:
            raise ValidationError("The name cannot have more than 50 characters")