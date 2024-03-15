{
    'name': 'Tele Users Login History',
    'version': '17.0',
    'category': 'Sales/CRM',
    'summary': 'Tele Users Login History',
    'author': 'INKERP',
    'website': 'https://www.telenoc.org/',
    'depends': ['base', 'mail'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/user_attendance.xml',
    ],
    
    'images': ['static/description/banner.jpeg'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
