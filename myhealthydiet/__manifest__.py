# -*- coding: utf-8 -*-
{
    'name': "MyHealthyDiet Management",

    'summary': """
        Diets and plates for a good nourishment""",

    'description': """
        This module is made for the purpose of having a good alimentation.
        You can manage:
        - Diets
        - Plates
        - Ingredients
        - Tips
        - Users. 
    """,

    'author': "QuickDiets",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/plateView.xml',        
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}