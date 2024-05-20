# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'author': 'Reliution',
    'version': '17.0',
    'license': 'LGPL-3',
    'sequence': 1,
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             # 'security/security.xml',
             # 'data/cron.xml',
             # 'wizard/appointment_view.xml',
             'views/property_view.xml',
             # 'views/estate_property.xml',
             # 'views/property_tag.xml',
             # 'views/property_type.xml',
             # 'views/inherite_field.xml',
             'report/quotation.xml',
             'report/report_view.xml'
             ],
    'auto_install': False,
    'application': True,
    'installable': True,
}
