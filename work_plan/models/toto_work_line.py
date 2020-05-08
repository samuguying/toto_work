from odoo import models, fields, api


class WorkLine(models.Model):
    _name = 'toto.work.line'

    name = fields.Char('线别名称', required=True)

    _sql_constraints = [
        ("name_uniq", "unique (name)", "名称不能重复！"),
    ]
