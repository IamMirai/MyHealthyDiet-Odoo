# -*- coding: utf-8 -*-

from odoo import models, fields

class weight(models.Model):
    _name = 'myhealthydiet.weight'

#   VARIABLES
    weight_id = fields.Integer(required=True, help="Id of the weight")
    weight = fields.Float(required=True, help="Weight of the client")
    date = fields.Date(required=True, help="Time when the weight is registered")