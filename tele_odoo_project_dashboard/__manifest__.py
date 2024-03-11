# -*- coding: utf-8 -*-
{
    'name': 'Tele Odoo Project Dashboard',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Get a Detailed View for Project.""",
    'description': """In this dashboard user can get the Detailed Information 
     about Project, Task, Employee, Hours recorded, Total Margin and Total 
     Sale Orders.""",
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'website': 'https://www.telenoc.org',
    'depends': ['sale_management', 'project', 'sale_timesheet'],
    'data': ['views/dashboard_views.xml'],
    'assets': {
        'web.assets_backend': [
            'project_dashboard_odoo/static/src/js/dashboard.js',
            'project_dashboard_odoo/static/src/css/dashboard.css',
            'project_dashboard_odoo/static/src/xml/dashboard_templates.xml',
            'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js'
        ]},
    'images': ['static/description/banner.jpeg'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
