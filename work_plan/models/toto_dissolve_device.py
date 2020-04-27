from odoo import models, fields, api


class DissolveDevice(models.Model):
    _name = 'toto.dissolve.device'

    name = fields.Char('设备名称', required=True)

    _sql_constraints = [
        ("name_uniq", "unique (name)", "名称不能重复！"),
    ]
