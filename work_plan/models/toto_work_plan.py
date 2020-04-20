from odoo import models, fields, api


class WorkPlan(models.Model):
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _name = 'toto.work.plan'

    date = fields.Datetime('Date', default=fields.Datetime.now)
    class_id = fields.Many2one('toto.work.class.type', 'Class Type')
    work_type = fields.Selection([('night', '夜班'), ('day', '白班')])
    vacation = fields.Char('Vacation', default='无')
    staffing = fields.Integer('Staffing', compute='_compute_staffing')
    item_ids = fields.One2many('toto.work.plan.item', 'plan_id', 'Staffing')

    @api.depends('item_ids')
    def _compute_staffing(self):
        for work_plan in self:
            if work_plan.item_ids:
                work_plan.staffing = len(work_plan.item_ids)
            else:
                work_plan.staffing = 0


class WorkPlanItem(models.Model):
    _name = 'toto.work.plan.item'

    sequence = fields.Integer(string="Sequence", default=10)
    plan_id = fields.Many2one('toto.work.plan', 'Plan')
    device_id = fields.Many2one('toto.work.device', 'Device Name')
    user_id = fields.Many2one('res.users', 'User')
    work_subject = fields.Char('Subject')
    predetermined_quantity = fields.Integer('Predetermined Quantity')
    actual_quantity = fields.Integer('Actual Quantity')
    note = fields.Text('Note')

    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    name = fields.Char(string="Name")
