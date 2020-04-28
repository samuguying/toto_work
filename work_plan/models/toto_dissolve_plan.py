from odoo import models, fields, api


class DissolvePlan(models.Model):
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _name = 'toto.dissolve.plan'

    date = fields.Datetime('日期', default=fields.Datetime.now)
    line_id = fields.Char('线别')
    staffing = fields.Integer('人员配置')
    vacation = fields.Char('休假', default='无')

    class DissolvePlanItem(models.Model):
        _name = 'toto.dissolve.plan.item'

        sequence = fields.Integer(string="Sequence", default=10)
        plan_id = fields.Many2one('toto.dissolve.plan', '计划')
        device_id = fields.Many2one('toto.dissolve.device', '设备')
        dissovle_pinben= fields.Char('品番')
        predetermined_quantity = fields.Integer('预定数量')
        actual_quantity = fields.Integer('实际数量')
        note = fields.Text('备注')

        display_type = fields.Selection([
            ('line_section', "Section"),
            ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
        name = fields.Char(string="名称")