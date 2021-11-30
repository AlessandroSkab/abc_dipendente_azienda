# -*- coding: utf-8 -*-
{
    'name': "Campo Nominativo di riferimento in Ordine di vendita",

    'summary': """
        Modulo che estende la vista del sale.view_order_form e permette l'aggiunta di un
        campo relazionale il quale in base al Cliente selezionato ti permette di scegliere
        un dipendente della stessa Azienda.""",

    'description': """
        Modulo che estende la vista del sale.view_order_form e permette l'aggiunta di un
        campo relazionale il quale in base al Cliente selezionato ti permette di scegliere
        un dipendente della stessa Azienda.
    """,

    'author': "A.B.C. Strategie",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
