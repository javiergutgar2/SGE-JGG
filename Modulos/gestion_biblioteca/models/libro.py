# -*- coding: utf-8 -*-
from odoo import models, fields, api
class gestion_biblioteca(models.Model):
    _name = 'gestion_biblioteca.libro'
    _description = 'Libro (Biblioteca)'
    name = fields.Char(string="Título", required=True, help="Introduce el título del libro")
    autor = fields.Many2one('gestion_biblioteca.autor', string="Autor")
    idioma = fields.Selection(
        [
            ('es', 'Español'),
            ('en', 'Inglés'),
            ('fr', 'Francés'),
            ('cat', 'Catalán'),
        ],
        string="Idioma",
        required=True,
        default='es'
    )
    active = fields.Boolean(string = "Activo", default=True)
    isbn = fields.Char(string="ISBN", required=True, help="Introduce el ISBN")
    fecha = fields.Date(string="Fecha de adquisición")
    description = fields.Text(string="Descripción")
    portada = fields.Image(string="Portada")
    

    @api.depends('value')
    def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100

