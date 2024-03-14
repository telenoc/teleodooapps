# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "Tele Web Window Title",
    'summary': "The custom web window title",
    'author': "TeleNoc",
    'website': "https://telenoc.org",
    'support': 'contact@telenoc.org',
    'category': 'Extra Tools',
    'version': '1.1',
    'depends': ['base_setup'],
    'demo': [
        'data/demo.xml',
    ],
    'data': [
        'views/res_config.xml',
    ],
    'images': [
        'static/description/banner.jpeg',
    ],
    'assets': {
        'web.assets_backend': [
            'web_window_title/static/src/js/web_window_title.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}