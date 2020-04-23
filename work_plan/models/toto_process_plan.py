from odoo import models, fields, api


class ProcessPlan(models.Model):
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _name = 'toto.process.plan'

    name = fields.Char('名称')