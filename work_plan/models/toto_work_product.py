from odoo import models, fields, api


class Product(models.Model):
    _name = 'toto.work.plan.product'
    _rec_name = 'code'

    code = fields.Char('品番', required=True)
    name = fields.Char('名称')
    type = fields.Selection([
        ("shaping", "成形"),
        ("dissolve", "溶着"),
    ], string="系别")
    work_subject_id = fields.Many2one("toto.work.subject", string='作业项目')
    shaping_product_ids = fields.Many2many("toto.work.plan.product",
                                           relation="toto_work_plan_product_shaping_rel",
                                           column1="product_id", column2="shaping_product_id",
                                           domain=[('type', '=', "shaping")],
                                           string="成形品番")
    apply_to_products = fields.Char(string="对应制品")

    _sql_constraints = [
        ("code_uniq", "unique (code)", "品番不能重复！"),
    ]
