# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tip(models.Model):
    _name = 'myhealthydiet.tip'

    name = fields.Char(string="Tip", required=True, help="Name of the tip")
    tipText = fields.Text(string="Tip Text",required=True,help="The text a tip contains")
    tipType = fields.Selection([("app","App"),("nutrition","Nutrition")],string="Tip Type",help="The type of the tip: App or Nutrition")
    diet_id = fields.Many2one('myhealthydiet.diet', ondelete='set null')