# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class Diet(models.Model):
#   MODEL CONFIG
    _name = 'myhealthydiet.diet'

#   VARIABLES
    name = fields.Char(string='Diet', required=True, help="Diet name")
    description = fields.Text(string='Description', required=True, help="Description")
    carbohydrates = fields.Float(string='Carbohydrates', required=True, help="Carbohydrates")
    calories = fields.Float(string='Calories', required=True, help="Calories")
    proteins = fields.Float(string='Proteins', required=True, help="Proteins")
    lipids = fields.Float(string='Lipids', required=True, help="Lipids")
    goalType = fields.Selection([('INCREASE', 'INCREASE'), ('DECREASE', 'DECREASE'), ('MANTAIN', 'MANTAIN')], string='Goal', required=True, help="Goal")
    
#   RELATIONS
    tip_ids = fields.One2many('myhealthydiet.tip', 'diet_id', string="Tips", required=True, help="Tips")
    plate_ids = fields.One2many('myhealthydiet.plate','diet_id', string="Plates", required=True, help="Plates")
    user_ids = fields.Many2many('res.users', string="Users", required=True, help="Users")
    
    
    #VALIDATIONS
    @api.onchange ('carbohydrates', 'calories', 'proteins', 'lipids')
    def _onchange_1 (self):
        if self.carbohydrates < 0.0 or self.calories < 0.0 or self.proteins < 0.0 or self.lipids < 0.0:
            return{
                'warning': {
                    'title': "Something bad happened",
                    'message': "Value can not be less than 0",
                }
            }
    
    @api.onchange ('carbohydrates', 'proteins', 'lipids')
    def _onchange_2 (self):
        if self.carbohydrates > self.calories or self.proteins > self.calories or self.lipids > self.calories:
            return{
                'warning': {
                    'title': "Something bad happened",
                    'message': "Value can not be greater than calories value",
                }
            }  
            
    @api.constrains ('carbohydrates', 'calories', 'proteins', 'lipids')
    def _check_1 (self):
        if self.carbohydrates < 0.0 or self.calories < 0.0 or self.proteins < 0.0 or self.lipids < 0.0:
            raise ValidationError ("Your record" + " Carbohydrates: " + str(self.carbohydrates) + " or Proteins: " + str(self.proteins) + " or Lipids: " + str(self.lipids) + " or Calories: " + str(self.calories) + " can not be less than 0")

    @api.constrains ('carbohydrates', 'calories', 'proteins', 'lipids')
    def _check_2 (self):
        if self.carbohydrates > self.calories or self.proteins > self.calories or self.lipids > self.calories:
            raise ValidationError ("Your record" + " Carbohydrates: " + str(self.carbohydrates) + " or Proteins: " + str(self.proteins) + " or Lipids: " + str(self.lipids) + " can not be greater than " + " Calories: " + str(self.calories))