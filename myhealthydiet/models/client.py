# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Client(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    age = fields.Integer(string="Age",required=True,help="The clients current age")
    genre = fields.Selection([("male","Male"),("female","Female"),("non_binary","Non Binary")],string="Genre",help="The clients genre: male,female or non binary")
    goal = fields.Selection([("increase","Increase"),("decrease","Decrease"),("maintain","Maintain")],string="Goal",help="The clients goal: increase, decrease or maintain")
    height = fields.Float(string="Height",required=True,help="The clients current age")
    weights = fields.One2many("myhealthydiet.weight","user_id",string="Weights")
    diets = fields.Many2many("myhealthydiet.diet")
    
    @api.onchange('age')
    def _onchange_age(self):
        if self.age > 99 or self.age < 15:
            return {
                'warning': {
                    'title': "Incorrect 'age' value",
                    'message': "The age cannot be higher than 99 or lower than 15",
                },
            }
            
    @api.constrains('age')
    def _constrains_age(self):
        for record in self:
            if record.age > 99 or self.age < 15:
                raise ValidationError("The age cannot be higher than 99 or lower than 15")
            
    @api.onchange('height')
    def _onchange_height(self):
        if self.height > 2.50:
            return {
                'warning': {
                    'title': "Incorrect 'height' value",
                    'message': "The heaight value cannot be higher than 2.50",
                },
            }
    
    @api.constrains('height')
    def _constrains_height(self):
        for record in self:
            if record.height > 2.50:
                raise ValidationError("The heaight value cannot be higher than 2.50")