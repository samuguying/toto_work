from datetime import datetime

from odoo import models, fields, api


class WorkPlanDissolve(models.Model):
    _inherit = ["toto.work.plan"]
    _name = 'toto.dissolve.plan'

    def _default_assume_employee_id(self):
        employees = self.env.user.employee_ids
        if employees:
            return employees[0]
        else:
            return None

    assume_employee_id = fields.Many2one('hr.employee', '担当', default=_default_assume_employee_id)
    class_type_id = fields.Many2one('hr.department', related="assume_employee_id.department_id")
    item_ids = fields.One2many("toto.dissolve.plan.item", "dissolve_plan_id")
    note = fields.Text('备注')
    state = fields.Selection([
        ('progress', '进行中'),
        ('done', '完成'),
    ], string='状态', compute="_compute_state", store=True)

    @api.depends("item_ids", "item_ids.state")
    def _compute_state(self):
        for dissolve in self:
            if all([item.state == 'done' for item in dissolve.item_ids]):
                dissolve.state = "done"
            else:
                dissolve.state = "progress"


class WorkPlanDissolveItem(models.Model):
    _inherit = 'toto.work.plan.item'
    _name = 'toto.dissolve.plan.item'

    dissolve_plan_id = fields.Many2one("toto.dissolve.plan", "溶着系计划")
    device_id = fields.Many2one('toto.work.device', '设备', ondelete="restrict",
                                domain="[('device_type','=','dissolve')]")
    product_id = fields.Many2one('toto.work.plan.product', '作业内容(品番)', ondelete="restrict")
    staff_ids = fields.One2many("hr.employee", "dissolve_item_id", string="作业员")
    staffing = fields.Integer('人数配置', compute="_compute_staffing")
    state = fields.Selection([
        ('progress', '进行中'),
        ('done', '完成'),
    ], string='状态', copy=False, default='progress', readonly=True, required=True)

    @api.depends("staff_ids")
    def _compute_staffing(self):
        for item in self:
            if item.staff_ids:
                item.staffing = len(item.staff_ids)
            else:
                item.staffing = 0

    def action_finish(self):
        self.ensure_one()
        self.state = 'done'


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    dissolve_item_id = fields.Many2one("toto.dissolve.plan.item")
