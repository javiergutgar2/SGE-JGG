# -*- coding: utf-8 -*-
# from odoo import http


# class JggReuniones(http.Controller):
#     @http.route('/jgg_reuniones/jgg_reuniones', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jgg_reuniones/jgg_reuniones/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jgg_reuniones.listing', {
#             'root': '/jgg_reuniones/jgg_reuniones',
#             'objects': http.request.env['jgg_reuniones.jgg_reuniones'].search([]),
#         })

#     @http.route('/jgg_reuniones/jgg_reuniones/objects/<model("jgg_reuniones.jgg_reuniones"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jgg_reuniones.object', {
#             'object': obj
#         })

