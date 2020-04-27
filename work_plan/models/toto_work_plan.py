from odoo import models, fields, api


class WorkPlan(models.Model):
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _name = 'toto.work.plan'

    date = fields.Datetime('日期', default=fields.Datetime.now)
    class_id = fields.Many2one('toto.work.class.type', '班别', ondelete="restrict")
    work_type = fields.Selection([ ('day', '早班'),('middle', '中班'),('night', '夜班')],string="班次")
    vacation = fields.Char('休假', default='无')
    staffing = fields.Integer('人员配置')
    item_ids = fields.One2many('toto.work.plan.item', 'plan_id', '人员安排')


class WorkPlanItem(models.Model):
    _name = 'toto.work.plan.item'

    sequence = fields.Integer(string="Sequence", default=10)
    plan_id = fields.Many2one('toto.work.plan', '计划', ondelete="cascade")
    device_id = fields.Many2one('toto.work.device', '设备', ondelete="restrict")
    user_id = fields.Many2one('res.users', '作业员', ondelete="restrict")
    work_subject = fields.Char('作业项目')
    predetermined_quantity = fields.Integer('预定数量')
    actual_quantity = fields.Integer('实际数量')
    note = fields.Text('备注')

    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    name = fields.Char(string="名称")
