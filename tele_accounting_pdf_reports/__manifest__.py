# -*- coding: utf-8 -*-

{
    'name': 'Tele Odoo 17 Accounting Financial Reports',
    'version': '17.0.1.0',
    'category': 'Invoicing Management',
    'description': 'Accounting Reports For Odoo 17, Accounting Financial Reports, '
                   'Tele Odoo 17 Financial Reports',
    'summary': 'Tele Accounting Reports For Odoo 17',
    'sequence': '1',
    'author': 'TeleNoc',
    'license': 'LGPL-3',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'support': 'contact@telenoc.org',
    'website': 'https://www.telenoc.org',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'data/account_account_type.xml',
        'views/menu.xml',
        'views/ledger_menu.xml',
        'views/financial_report.xml',
        'views/settings.xml',
        'wizard/account_report_common_view.xml',
        'wizard/partner_ledger.xml',
        'wizard/general_ledger.xml',
        'wizard/trial_balance.xml',
        'wizard/balance_sheet.xml',
        'wizard/profit_and_loss.xml',
        'wizard/tax_report.xml',
        'wizard/aged_partner.xml',
        'wizard/journal_audit.xml',
        'report/report.xml',
        'report/report_partner_ledger.xml',
        'report/report_general_ledger.xml',
        'report/report_trial_balance.xml',
        'report/report_financial.xml',
        'report/report_tax.xml',
        'report/report_aged_partner.xml',
        'report/report_journal_audit.xml',
        'report/report_journal_entries.xml',
    ],
    'pre_init_hook': '_pre_init_clean_m2m_models',
    'images': ['static/description/banner.jpg'],
}

# todo nys settings page
