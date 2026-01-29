# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class reunion(models.Model):
    _name = 'reuniones.reunion'
    _description = 'Reunión (Reuniones)'
    name = fields.Char('Reunión', required=True)
    fecha_inicio = fields.Date('Fecha de inicio')
    fecha_finalizacion = fields.Date('Fecha de finalización', compute='_calcular_fecha_finalizacion')
    duracion = fields.Integer('Duración de la reunión', help='Duración en días', default = 1)
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

    @api.constrains('duracion')
    def _check_duracion(self):
        for record in self:
            if record.duracion <= 0:
                raise ValidationError("La duración mínima es de 1 día.")

    @api.constrains('asientos', 'asistentes')
    def _check_asientos(self):
        for record in self:
            if record.asientos and record.asientos < 2:
                raise ValidationError("Mínimo 2 asistentos en la reunión")
            if record.asientos and len(record.asistentes) > record.asientos:
                raise ValidationError(f"No puede haber más asistentes ({len(record.asistentes)}), que número de asientos ({record.asientos})")


    @api.depends('fecha_inicio', 'duracion')
    def _calcular_fecha_finalizacion(self):
        for reunion in self:
            if reunion.fecha_inicio and reunion.duracion:
                reunion.fecha_finalizacion = reunion.fecha_inicio + timedelta(days=reunion.duracion)
            else:
                reunion.fecha_finalizacion = None


