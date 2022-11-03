# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models
from odoo.tools.translate import _


class GarajeCoche(models.Model):
    _name = 'garaje.coche'
    _description = "garaje.coche"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order ='name'

    #model fields
    name = fields.Char(
        string = "Matricula",
        required = True,
        size = 7,
    )
    descripcion = fields.Text(
        string = "Descripcion",
    )
    modelo = fields.Char(
        string = "Modelo",
        required = True,
    )
    construido = fields.Date(
        string="Fecha del modelo",
    )
    consumo = fields.Float(
        'Consumo', #string -> no permite la etiqueta string al ser float.
        (4,1), #limit
        default= 0.0, 
        help ='Consumo promedio de cada 100 kms'
    )
    averiado = fields.Boolean(
        string = "Averiado",
        default = False
    )
    #relational fields
    aparcamientoId = fields.Many2one(comodel_name='garaje.aparcamiento', string='Aparcamiento')
    mantenimientoIds = fields.Many2many(comodel_name='garaje.mantenimiento', string='Mantenimiento')
