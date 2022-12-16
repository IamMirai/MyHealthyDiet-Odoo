# -*- coding: utf-8 -*-

from odoo import models, fields

class weight(models.Model):
    _name = 'myhealthydiet.weight'

    weight_id = fields.Integer()
    weight = fields.Float()
    date = fields.Date()
