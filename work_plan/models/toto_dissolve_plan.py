from datetime import datetime

from odoo import models, fields, api


class WorkPlanDissolve(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = 'toto.dissolve.plan'

    assume_user_id = fields.Many2one('res.users', '担当', default=lambda self: self.env.user)
    date = fields.Datetime('日期', default=fields.Datetime.now)
    device_id = fields.Many2one('toto.work.device', '设备', ondelete="restrict", domain="[('device_type','=','dissolve')]")
    staffing = fields.Integer('人员配置')
    product_id = fields.Many2one('toto.work.plan.product', '作业内容(品番)', ondelete="restrict")
    predetermined_quantity = fields.Integer('预定数量', default=None)
    actual_quantity = fields.Integer('实际数量', default=None)
    note = fields.Text('备注')
    state = fields.Selection([
        ('process', '未完成'),
        ('finished', '完成'),
    ], default='process', string='达成情况')

    @api.multi
    def name_get(self):
        return [(dissolve.id, "%s-%s" % (dissolve.device_id.name, datetime.strftime(dissolve.date, "%Y年%m月%d日"))) for dissolve in self]

    def action_finish(self):
        self.ensure_one()
        self.state = 'finished'

    def action_renew(self):
        self.ensure_one()
        self.state = 'process'
