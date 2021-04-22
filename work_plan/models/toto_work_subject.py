# _*_ coding: utf-8 _*_
from odoo import models, fields, api


class TotoWorkSubject(models.Model):
    _name = "toto.work.subject"
    _description = "作业内容"

    name = fields.Char(string="作业内容", required=True, index=True)

    _sql_constraints = [
        ("name_uniq", "unique (name)", "作业内容不能重复！"),
    ]
