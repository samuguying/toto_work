from odoo import models, fields, api


class WorkPowerPlan(models.Model):
    _inherit = "toto.work.plan"
    _name = 'toto.power.plan'

    item_ids = fields.One2many('toto.power.plan.item', 'power_plan_id', string='人员安排')


class WorkPowerPlanItem(models.Model):
    _inherit = "toto.work.plan.item"
    _name = 'toto.power.plan.item'

    power_plan_id = fields.Many2one('toto.power.plan', string='动力系计划', ondelete="cascade")

    state = fields.Selection([
        ('progress', '进行中'),
        ('done', '完成'),
        ('cancel', '终止'),
    ], string='状态', copy=False, default='progress', readonly=True, required=True)

    def action_finish(self):
        self.ensure_one()
        self.state = 'done'

    def action_cancel(self):
        self.ensure_one()
        self.state = 'cancel'
