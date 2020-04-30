from odoo import models, fields, api


class Product(models.Model):
    _name = 'toto.work.plan.product'
    _rec_name = 'code'

    name = fields.Char('名称')
    code = fields.Char('品番')

    def name_get(self):
        return [(p.id, p.code) for p in self]
