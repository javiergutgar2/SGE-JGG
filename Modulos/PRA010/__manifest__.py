# -*- coding: utf-8 -*-
{
    'name': "- Gestión de la sala de reuniones (Javier Gutiérrez García)",

    'summary': "Módulo para la gestión de las salas de reuniones de la empresa",

    'description': """
En este módulo guardaremos la información de las salas y de las reuniones que se harán en ellas.
    """,

    'author': "Javier Gutiérrez García",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/reunion_views.xml',
        'views/sala_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

