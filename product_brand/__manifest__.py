# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Product Brand',
    'version': '1.0',
    'summary': 'Module for Product Brand',
    'sequence': 10,
    'description': """Demo Software""",
    'category': 'Productivity',
    'depends': ['product', 'point_of_sale', 'sale'],
    'data': [
        'views/product_brand.xml',
        'views/assets.xml',
    ],
    'demo': [],
    'qweb': ['static/src/xml/product.xml',
             'static/src/xml/receipt.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
