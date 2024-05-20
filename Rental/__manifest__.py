# -*- coding: utf-8 -*-
{
    'name': 'Rental',
    'author': 'Cloud',
    'version': '17.0',
    'license': 'LGPL-3',
    'sequence': 1,
    'depends': ['base','sale','sale_renting'],
    'data': ['views/rental.xml',
             'report/challan_report_inherit.xml'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
