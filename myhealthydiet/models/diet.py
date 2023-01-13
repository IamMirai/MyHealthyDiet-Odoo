# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
    goalType = fields.Selection([('INCREASE', 'INCREASE'),('DECREASE','DECREASE'),('MANTAIN','MANTAIN')],string='Goal', required=True, help="Goal")
    
#   RELATIONS
    tip_ids = fields.One2many('myhealthydiet.tip', 'diet_id', string="Tips", required=True, help="Tips")
    plate_ids = fields.One2many('myhealthydiet.plate','diet_id', string="Plates", required=True, help="Plates")
    user_ids = fields.Many2many('res.users', string="Users", required=True, help="Users")
    