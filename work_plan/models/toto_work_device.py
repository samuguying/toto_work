from odoo import models, fields, api


class WorkDevice(models.Model):
    _name = 'toto.work.device'

    name = fields.Char('Device Name', required=True)
