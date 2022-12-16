# -*- coding: utf-8 -*-

from odoo import models, fields

class plate(models.Model):
    _name = 'myhealthydiet.plate'
    
    plate_id = fields.Integer(required=True, help="Id of the plate")
    plateName = fields.Char(required=True, help="Name of the plate")
    mealType = fields.Selection([("BREAKFAST", "BREAKFAST"), ("LUNCH", "LUNCH"), ("DINNER", "DINNER")], required=True, 
    help="Type of meal: Breakfast, Lunch, Dinner")
    calories = fields.Float(required=True, help="Calories of the plate")
    carbohydrates = fields.Float(required=True, help="Carbohydrates of the plate")
    lipids = fields.Float(required=True, help="Lipids of the plate")
    proteins = fields.Float(required=True, help="Proteins of the plate")
    isVegetarian = fields.Boolean(required=True, help="Defines if the plate is vegetarian or not")
    
    ingredients = fields.Many2many('myhealthydiet.ingredient')
    diets = fields.Many2many('myhealthydiet.diet')