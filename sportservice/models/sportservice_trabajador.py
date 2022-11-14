# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SportServiceTrabajador(models.Model):
    _name ='sportservice.trabajador'
    _description = 'Creacion de trabajador'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # models fields 
    name = fields.Char(
        string="Nombre",
        required = True,
    )
    birthDate = fields.Date(
        string="Fecha de nacimiento",
        default = fields.date.today(),
        required = True,
     )

    email = fields.Char(
        string="Correo electrónico",
        required = True,
        #compute = '_get_value_mail',
     )
    phone = fields.Char(
        string="Teléfono",
    )
    attachment = fields.Binary(
        string="Imagen de perfil",
    )    
    store_fname = fields.Char(
        string="File Name",
    )

    cv = fields.Binary(
        string="Curriculum Vitae",
    )

    

  #  @api.multi
   # @api.depends('email')

    #def _get_value_mail(self):
     #   pass
