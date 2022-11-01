# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _


class GarajeAparcamiento(models.Model):
    _name = 'garaje.aparcamiento'
    _description = "garaje.aparcamiento"

    name = fields.Char(
        string="Dirección",
        required=True,
    )
    plazas=fields.Integer(
        string="Plazas",
        required=True,
    )
