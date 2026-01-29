# -*- coding: utf-8 -*-

from odoo import models, fields, api
class reunion(models.Model):
    _name = 'reuniones.reunion'
    _description = 'Reunión (Reuniones)'
    name = fields.Char('Reunión', required=True)
    fecha_inicio = fields.Date('Fecha de inicio')
    duracion = fields.Integer('Duración de la reunión', help='Duración en días')
    sala = fields.Many2one("reuniones.sala",ondelete='cascade', string = "Sala de Reunion", required=True)
    asientos = fields.Integer('Número de asientos')
    responsable = fields.Many2one("res.partner", string = "Responsable de la Reunión")
    asistentes = fields.Many2many('res.partner', string="Asistentes a la Reunión")
    asientos_ocupados = fields.Float(compute='_calcular_asientos_ocupados', string = "Asientos ocupados", store=True)

    @api.depends('asientos', 'asistentes')
    def _calcular_asientos_ocupados(self):
        for reunion in self:
            if not reunion.asientos:
                reunion.asientos_ocupados = 0.0
            else:
                reunion.asientos_ocupados = 100.0 * len(reunion.asistentes) / reunion.asientos
