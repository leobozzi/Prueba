# -*- coding: utf-8 -*-
{
    'name': "Garaje",

    'summary': """""",

    'description': """
        Este módulo administra garajes:
            - 
            - 
            - 
            - 
            -
    """,

    'author': "Leonardo Bozzi",
    'website': "http://www.vangrow.ar",

    # for the full list
    'category': 'Garaje',
    'version': '1.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail',
    ],

    # always loaded
    'data': [
        'security/garaje_security.xml',
        'security/ir.model.access.csv',
        'view/garaje_view.xml',
        'view/garaje_aparcamiento_view.xml',
        'security/garaje_security_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
