# -*- coding: utf-8 -*-
# from odoo import http


# class HabitosSaludables(http.Controller):
#     @http.route('/habitos_saludables/habitos_saludables', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/habitos_saludables/habitos_saludables/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('habitos_saludables.listing', {
#             'root': '/habitos_saludables/habitos_saludables',
#             'objects': http.request.env['habitos_saludables.habitos_saludables'].search([]),
#         })

#     @http.route('/habitos_saludables/habitos_saludables/objects/<model("habitos_saludables.habitos_saludables"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('habitos_saludables.object', {
#             'object': obj
#         })

