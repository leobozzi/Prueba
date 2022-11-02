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
        require = True,
        size = 7,
    )
    descripcion = fields.Text(
        string = "Descripcion",
    )
    modelo = fields.Char(
        string = "Modelo",
        require = True,
    )
    construido = fields.Date(
        string="Fecha del modelo",
    )
    consumo = fields.Float('Consumo', (4,1), default= 0.0, help ='Consumo promedio de cada 100 kms')
    #consumo = fields.Float(
        #(4,1), #limit
        #string='Consumo',
        #default= 0.0, 
        #help ='Consumo promedio de cada 100 km',
    #)
    averiado = fields.Boolean(
        string = "Averiado",
        default = False
    )
