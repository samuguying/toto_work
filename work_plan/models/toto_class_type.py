from odoo import models, fields, api


class ClassType(models.Model):
    _name = 'toto.work.class.type'

    name = fields.Char('Name', required=True)
