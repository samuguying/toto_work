from odoo import models, fields, api


class WorkPlanDissolve(models.Model):
    _inherit = 'toto.work.plan'
    _name = 'toto.dissolve.plan'

    assume_user_id = fields.Many2one('res.users', '担当', default=lambda self: self.env.user)
    item_ids = fields.One2many('toto.dissolve.plan.item', 'dissolve_plan_id', string='人员安排', ondelete="cascade")
    state = fields.Selection([
        ('process', '未完成'),
        ('finished', '完成'),
    ], default='process', string='达成情况')
    # employee_ids = fields.One2many('hr.employee', string="作业员",
    #                                related='assume_user_id.employee_ids.child_ids')

    def action_finish(self):
        self.ensure_one()
        self.state = 'finished'

    def action_renew(self):
        self.ensure_one()
        self.state = 'process'


class WorkPlanDissolveItem(models.Model):
    _inherit = 'toto.work.plan.item'
    _name = 'toto.dissolve.plan.item'

    product_id = fields.Many2one('toto.work.plan.product', '作业内容(品番)', ondelete="restrict")
    dissolve_plan_id = fields.Many2one('toto.dissolve.plan', '溶着系计划')
    operator = fields.Many2one('res.users', '作业员',)
