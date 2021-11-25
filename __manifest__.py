# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Components Requisition',
    'version': '1.0',
    'summary': 'Module Request of Components',
    'sequence': 10,
    'description': """Components Request Software""",
    'category': 'Productivity',
    'depends': ['purchase', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/request_sequence.xml',
        'views/component_request.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
