from odoo import models, fields, api


class DissolvePlan(models.Model):
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _name = 'toto.dissolve.plan'

    date = fields.Datetime('日期', default=fields.Datetime.now)

