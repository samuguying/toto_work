from odoo import models, fields, api


class WorkPowerPlan(models.Model):
    _inherit = "toto.work.plan"
    _name = 'toto.power.plan'

    create_user_id = fields.Many2one("res.users", "创建人", default=lambda self: self.env.user, readonly=True)
    project = fields.Char("作业项目", track_visibility='onchange', required=True)
    content = fields.Char("作业内容", track_visibility='onchange', required=True)
    user_id = fields.Many2one("res.users", string='作业者', ondelete="restrict",
                              domain="[('id', 'in', users_id)]")
    priority = fields.Selection([
        ('0', '很低'),
        ('1', '低'),
        ('2', '中'),
        ('3', '高'),
    ], string="优先级", default='1', track_visibility='onchange')
    plan_time = fields.Datetime("计划时间", track_visibility='onchange')
    finish_time = fields.Datetime("完成时间", readonly=True, track_visibility='onchange')
    duration = fields.Float("持续时间", digits=(3, 1))
    note = fields.Text("备注")
    power_item_ids = fields.One2many("toto.power.plan.item", "power_plan_id")
    state = fields.Selection([
        ('draft', '新的'),
        ('process', '进行中'),
        ('done', '完成'),
        ('cancel', '结束'),
    ], default="draft", string="状态", track_visibility='onchange')

    def name_get(self):
        return [(p.id, "%s" % (p.project, )) for p in self]

    def action_start(self):
        self.ensure_one()
        self.state = "process"

    def action_done(self):
        self.ensure_one()
        self.write({
            'state': 'done',
            'finish_time': fields.datetime.now()
        })

    def action_cancel(self):
        self.ensure_one()
        self.state = "cancel"


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
