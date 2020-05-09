from odoo import models, fields, api


class WorkPlanShaping(models.Model):
    _inherit = 'toto.work.plan'
    _name = 'toto.shaping.plan'

    bad_content = fields.Text('不良内容')
    employee_ids = fields.Many2many('hr.employee', string='作业员', ondelete="restrict",
                                    domain="[('department_id', '=', class_type_id)]")
    detail_countermeasure = fields.Html('具体对策')
    item_ids = fields.One2many('toto.shaping.plan.item', 'shaping_plan_id', string='人员安排')


class WorkPlanShapingItem(models.Model):
    _inherit = 'toto.work.plan.item'
    _name = 'toto.shaping.plan.item'

    shaping_plan_id = fields.Many2one('toto.shaping.plan', '溶着系计划', ondelete="cascade")
