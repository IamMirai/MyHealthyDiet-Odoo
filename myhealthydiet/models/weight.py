# -*- coding: utf-8 -*-

from odoo import models, fields

class Weight(models.Model):
    _name = 'myhealthydiet.weight'

#   VARIABLES
    name = fields.Char(string="Weight", required=True, help="Name of the weight")
    weight = fields.Float(required=True, help="Weight of the client")
    date = fields.Date(required=True, help="Time when the weight is registered")
    user_id = fields.Many2one('res.users', ondelete='set null')