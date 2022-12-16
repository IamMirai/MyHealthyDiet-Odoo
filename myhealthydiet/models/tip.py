# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tip(models.Model):
    _name = 'myhealthydiet.tip'

    tip_id = fields.Integer(string="Tip Id",required=True,help="Tips identification number")
    tipText = fields.Text(string="Tip Text",required=True,help="The text a tip contains")
    tipType = fields.Selection([("app","App"),("nutrition","Nutrition")],string="Tip Type",help="The type of the tip: App or Nutrition")