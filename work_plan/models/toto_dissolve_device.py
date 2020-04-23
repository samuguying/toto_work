from odoo import models, fields, api


class DissolveDevice(models.Model):
    _name = 'toto.dissolve.device'

    name = fields.Char('设备名称', required=True)
