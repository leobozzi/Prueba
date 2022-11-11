# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SportServiceCliente(models.Model):
    _name ='sportservice.cliente'
    _description = 'Creacion de cliente'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # models fields 
    name = fields.Char(
        string="Nombre",
        required = True,
    )
    birthDate = fields.Date(
        string="Fecha de nacimiento",
        default = "10-11-2022",
        required = True,
     )

    email = fields.Char(
        string="Correo electrónico",
        required = True,
     )
    phone = fields.Integer(
        string="Teléfono",
    )
    profilePicture = fields.Image(
        string="Imagen",
    )