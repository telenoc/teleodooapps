# -*- coding: utf-8 -*-

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

BILLING_CRITERIA = [
    ('fixed', "Fixed Rate"),
    ('per_user', 'Based on the No. of users')
]


class BackupDeletionConfirmation(models.TransientModel):
    _name = "backup.deletion.confirmation"
    _description = 'Backup Deletion Confirmation Wizard'
    
    backup_id = fields.Many2one(comodel_name="backup.process.detail", string="Backup Process Detail")
    message = fields.Html(string="Message")
    
    
    def action_delete_backup_detail(self):
        for rec in self:
            _logger.info("======= backup_id ======== %r", rec.backup_id)
            rec.backup_id.unlink()
    