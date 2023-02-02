# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError   

class Plate(models.Model):
    _name = 'myhealthydiet.plate'
    
    #VARIABLES
    name = fields.Char(required=True, help="Name of the plate", string="Plate")
    mealType = fields.Selection([("BREAKFAST", "BREAKFAST"), ("LUNCH", "LUNCH"), ("DINNER", "DINNER")], required=True, 
    help="Type of meal: Breakfast, Lunch, Dinner")
    carbohydrates = fields.Float(string='Carbohydrates', required=True, help="Carbohydrates")
    calories = fields.Float(string='Calories', required=True, help="Calories")
    proteins = fields.Float(string='Proteins', required=True, help="Proteins")
    lipids = fields.Float(string='Lipids', required=True, help="Lipids")
    isVegetarian = fields.Boolean(required=True, help="Defines if the plate is vegetarian or not")
    
    #RELATIONS
    ingredients = fields.Many2many('myhealthydiet.ingredient')
    diet_id = fields.Many2many('myhealthydiet.diet', ondelete='set null')
    
    #VALIDATIONS
    @api.onchange('carbohydrates','calories','proteins','lipids')
    def _onchange_negative_nutritional_values(self):
        if self.carbohydrates < 0.0 or self.calories < 0.0 or self.proteins < 0.0 or self.lipids < 0.0:
            return{
                'warning': {
                    'title': "Negative nutritional values.",
                    'message': "The nutritional values can't be negative.",
            }
        }
        
    @api.onchange('carbohydrates','calories','proteins','lipids')
    def _onchange_nutritional_values(self):
        if self.carbohydrates > self.calories or self.proteins > self.calories or self.lipids > self.calories:
            return{
                'warning': {
                    'title': "Nutritional values above calories.",
                    'message': "The nutritional values can't be greater than calories.",
            }
        }
        
    @api.constrains('carbohydrates','calories','proteins','lipids')
    def _constrains_negative_nutritional_values(self):
        if self.carbohydrates < 0.0 or self.calories < 0.0 or self.proteins < 0.0 or self.lipids < 0.0:
            raise ValidationError("The nutritional values can't be negative.")
        
    @api.constrains('carbohydrates','calories','proteins','lipids')
    def _constrains_nutritional_values(self):
        if self.carbohydrates > self.calories or self.proteins > self.calories or self.lipids > self.calories:
            raise ValidationError("The nutritional values can't be greater than calories.")