from odoo import models, fields, api


class WorkPlanDissolve(models.Model):
    _inherit = 'toto.work.plan'
    _name = 'toto.dissolve.plan'

    line_id = fields.Many2one('toto.work.line', '线别')
    item_ids = fields.One2many('toto.dissolve.plan.item', 'dissolve_plan_id', string='人员安排', ondelete="cascade")


class WorkPlanDissolveItem(models.Model):
    _inherit = 'toto.work.plan.item'
    _name = 'toto.dissolve.plan.item'

    product_id = fields.Many2one('toto.work.plan.product', '作业内容(品番)', ondelete="restrict")
    dissolve_plan_id = fields.Many2one('toto.dissolve.plan', '溶着系计划')
