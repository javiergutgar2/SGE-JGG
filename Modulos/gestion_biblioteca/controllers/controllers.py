# -*- coding: utf-8 -*-
# from odoo import http


# class GestionBiblioteca(http.Controller):
#     @http.route('/gestion_biblioteca/gestion_biblioteca', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_biblioteca/gestion_biblioteca/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_biblioteca.listing', {
#             'root': '/gestion_biblioteca/gestion_biblioteca',
#             'objects': http.request.env['gestion_biblioteca.gestion_biblioteca'].search([]),
#         })

#     @http.route('/gestion_biblioteca/gestion_biblioteca/objects/<model("gestion_biblioteca.gestion_biblioteca"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_biblioteca.object', {
#             'object': obj
#         })

