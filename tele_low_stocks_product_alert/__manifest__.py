# -*- coding: utf-8 -*-
{
    'name': "Tele Product Low Stock Alert",
    'version': '17.0.1.0.0',
    "category": 'Warehouse,Point of Sale',
    'summary': """Product Low Stock Alert Display in Point of Sale and 
    Product Views""",
    'description': """Module adds functionality to display product stock 
    alerts in the point of sale interface, indicating low stock levels for 
    products and also in the product template kanban and list view.""",
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'website': 'https://www.telenoc.org',
    'depends': ['stock', 'point_of_sale'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'low_stocks_product_alert/static/src/css/template_color.css',
        ],
        'point_of_sale._assets_pos': [
            'low_stocks_product_alert/static/src/xml/product_item_template.xml',
            'low_stocks_product_alert/static/src/xml/product_list_template.xml',
        ],
    },
    'images': ['static/description/banner.jpeg'],
    'license': "LGPL-3",
    'installable': True,
    'application': False,
    'auto_install': False,
}
