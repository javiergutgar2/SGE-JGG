# -*- coding: utf-8 -*-

from odoo import models, fields, api
class sala(models.Model):
    _name = 'reuniones.sala'
    _description = 'Sala (Reuniones)'
    name = fields.Char('Sala', required=True)
    descripcion = fields.Text('Descripción', required=True)
    reuniones = fields.One2many("reuniones.reunion",  "name", string="Reuniones",required=True)
   

