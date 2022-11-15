# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SportServiceServicio(models.Model):
    _name ='sportservice.servicio'
    _description = 'Creacion de servicio'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # models fields 
    name = fields.Char(
        string="Nombre de servicio", 
        required = True,
    )

    serviceId = fields.Integer(
        string="Servicio Id",
        required = True,
    )
    description = fields.Text(
        string="Descripcion",
     )
     
    serviceImage = fields.Image(
        string="Imagen de servicio",
    )
    
    serviceInstallation = fields.Selection(
        string = "Instalacion de servicio",
        required = True,
        selection = [
            ('E1', 'Example 1'), 
            ('E2', 'Example 2'), 
            ('E3', 'Example 3'), 
        ],
        default = 'E1'
    )
    servicePrice= fields.Float(
        string="Valor de servicio"
    )
    duration = fields.Integer(
        string="Duracion de servicio(minutos)",
    )

    partnerIds = fields.Many2many(
        comodel_name= 'sportservice.cliente',
        string="Cliente",
    )
    employeeIds = fields.Many2many(
        comodel_name= 'sportservice.trabajador',
        string="Trabajador",
    )

    hours = fields.Selection(
        string = "Horario",
        required = True,
        selection = [
            ('17.00-17.30'), 
            ('18.00-18.30'), 
            ('19.00-19.30'),
            ('20.00-20.30'),
            ('21.00-21.30'),
            ('22.00-22.30'),
            ('23.00-23.30'),
        ],
    )
    
    days = fields.Selection(
        string = "Dias",
        required = True,
        selection = [
            ('Lunes'),
            ('Martes'),
            ('Miércoles'),
            ('jueves'),
            ('Viernes'),
        ],
    )


