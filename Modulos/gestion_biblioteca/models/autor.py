# -*- coding: utf-8 -*-
from odoo import models, fields, api
class gestion_biblioteca(models.Model):
    _name = 'gestion_biblioteca.autor'
    _description = 'Autor (Biblioteca)'
    name = fields.Char(string="Nombre", required=True, help="Nombre del autor")
    pais = fields.Many2one('res.country', string="País")
    libros = fields.One2many("gestion_biblioteca.libro",  "autor", string="Libros")