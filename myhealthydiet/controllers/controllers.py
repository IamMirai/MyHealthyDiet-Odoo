# -*- coding: utf-8 -*-
from odoo import http

# class Myhealthydiet(http.Controller):
#     @http.route('/myhealthydiet/myhealthydiet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myhealthydiet/myhealthydiet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myhealthydiet.listing', {
#             'root': '/myhealthydiet/myhealthydiet',
#             'objects': http.request.env['myhealthydiet.myhealthydiet'].search([]),
#         })

#     @http.route('/myhealthydiet/myhealthydiet/objects/<model("myhealthydiet.myhealthydiet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myhealthydiet.object', {
#             'object': obj
#         })