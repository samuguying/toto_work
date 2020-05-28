from odoo import models, fields, api


class Product(models.Model):
    _name = 'toto.work.plan.product'
    _rec_name = 'code'

    code = fields.Char('品番', required=True)
    name = fields.Char('名称')

    _sql_constraints = [
        ("code_uniq", "unique (code)", "品番不能重复！"),
    ]
