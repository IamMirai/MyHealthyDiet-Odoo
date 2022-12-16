# -*- coding: utf-8 -*-

from odoo import models, fields

class plate(models.Model):
    _name = 'myhealthydiet.plate'
    
    plate_id = fields.Integer(required=True, help="Id of the plate")
    plateName = fields.Char(required=True, help="Name of the plate")
    mealTypeEnum = fields.Selection([("BREAKFAST", "BREAKFAST"), ("LUNCH", "LUNCH"), ("DINNER", "DINNER")], required=True, 
    help="Type of meal: Breakfast, Lunch, Dinner")
    ingredients = fields.Many2many('myhealthydiet.ingredient')
    diets = fields.Many2many('myhealthydiet.diet')