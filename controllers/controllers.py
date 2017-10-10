# -*- coding: utf-8 -*-
from odoo import http

# class Ranchy(http.Controller):
#     @http.route('/ranchy/ranchy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ranchy/ranchy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ranchy.listing', {
#             'root': '/ranchy/ranchy',
#             'objects': http.request.env['ranchy.ranchy'].search([]),
#         })

#     @http.route('/ranchy/ranchy/objects/<model("ranchy.ranchy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ranchy.object', {
#             'object': obj
#         })