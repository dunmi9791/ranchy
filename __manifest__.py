 # -*- coding: utf-8 -*-
{
    'name': "ranchy",

    'summary': """
        this module is to run the daily activities of the ranchy community  """,

    'description': """
        coperative loans and savings 
    """,

    'author': "secteur network solutions",
    'website': "http://www.secteurnetworks.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'depends': ['mail'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
         'views/membersview.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}