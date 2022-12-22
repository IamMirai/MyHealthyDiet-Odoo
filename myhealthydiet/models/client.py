# -*- coding: utf-8 -*-

from odoo import models, fields, api

class client(models.Model):
    _inherit = 'res.users'

    age = fields.Integer(string="Age",required=True,help="The clients current age")
    genre = fields.Selection([("male","Male"),("female","Female"),("non_binary","Non Binary")],string="Genre",help="The clients genre: male,female or non binary")
    goal = fields.Selection([("increase","Increase"),("decrease","Decrease"),("maintain","Maintain")],string="Goal",help="The clients goal: increase, decrease or maintain")
    height = fields.Float(string="Height",required=True,help="The clients current age")
    weights = fields.One2Many("myhealthydiet.weight","user_id",string="Weights")
    diets = fields.Many2Many("myhealthydiet.diet")