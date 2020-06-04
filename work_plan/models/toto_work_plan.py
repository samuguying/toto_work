from odoo import models, fields, api


class WorkPlan(models.Model):
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _name = 'toto.work.plan'
    _rec_name = 'date'

    def _default_class_type_id(self):
        depts = self.env.user.employee_ids.mapped('department_id')
        if depts:
            return depts[0]
        else:
            return None

    date = fields.Datetime('日期', default=fields.Datetime.now)
    # class_id = fields.Many2one('toto.work.class.type', '班别', ondelete="restrict")
    class_type_id = fields.Many2one('hr.department', '班别', ondelete="restrict",
                                    default=_default_class_type_id,
                                    domain=lambda self: [('id', 'in', self.env.user.employee_ids.mapped('department_id').ids)])
    users_id = fields.One2many("res.users", compute="_compute_users")
    work_type = fields.Selection([('day', '早班'), ('middle', '中班'), ('night', '夜班')], string="班次")
    vacation = fields.Char('休假', default='无')
    staffing = fields.Integer('出勤人数')

    plan_type = fields.Selection([
        ('shaping', '成形系'),
        ('power', '动力系'),
        ('dissolve', '溶着系'),
        ('process', '加工系'),
    ])

    @api.depends("class_type_id")
    def _compute_users(self):
        for p in self:
            p.users_id = [(4, u.id) for u in p.class_type_id.mapped("member_ids.user_id")]
            for dept in p.class_type_id.child_ids:
                p.users_id = [(4, u.id) for u in dept.member_ids.mapped("user_id")]


class WorkPlanItem(models.Model):
    _name = 'toto.work.plan.item'

    sequence = fields.Integer(string="Sequence", default=10)
    device_id = fields.Many2one('toto.work.device', '设备', ondelete="restrict")
    employee_id = fields.Many2one('hr.employee', '作业员', ondelete="restrict")
    user_id = fields.Many2one("res.users", string='作业员', ondelete="restrict")
    work_subject = fields.Char('作业项目')
    predetermined_quantity = fields.Integer('预定数量', default=None)
    actual_quantity = fields.Integer('实际数量', default=None)
    note = fields.Text('备注')
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    name = fields.Char(string="名称")
