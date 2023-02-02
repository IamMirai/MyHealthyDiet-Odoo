# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Tip(models.Model):
    _name = 'myhealthydiet.tip'

    name = fields.Char(string="Tip id", required=True, help="Name of the tip")
    tipText = fields.Text(string="Tip Text",required=True,help="The text a tip contains")
    tipType = fields.Selection([("app","App"),("nutrition","Nutrition")],string="Tip Type",help="The type of the tip: App or Nutrition")
    diet_id = fields.Many2one('myhealthydiet.diet', ondelete='set null')
    
    #@api.onchange('tipText')
    #def _onchange_text(self):
    #    if len(self.tipText) > 100:
    #        return {
    #            'warning': {
    #                'title': "Incorrect 'Tip Text' value",
    #                'message': "The text cannot be higher than 100 characters",
    #            },
    #        }
            
    @api.constrains('tipText')
    def _constrains_text(self):
        if len(self.tipText) > 100:
            raise ValidationError("The text cannot be higher than 100 characters")